from fabric.api import env, run, task, prefix, cd, sudo, settings
from fabric.contrib.files import exists
from djangus.settings.common import SITE_NAME, BASE_DIR
from os.path import join, normpath
from os import environ

########## GLOBALS
env.run = 'python manage.py'
env.user = 'bjacobel'
env.hosts = ['citadel.bjacobel.com']
env.path = "/home/bjacobel/code/" + SITE_NAME
env.command_prefixes = [
    "cd /home/bjacobel/code/" + SITE_NAME,
    "source /home/bjacobel/.virtualenvs/{}/bin/activate".format(SITE_NAME),
    'export DJANGO_SETTINGS_MODULE={}.settings.prod'.format(SITE_NAME),
    'export {site}_SECRET_KEY=\'{key}\''.format(site=SITE_NAME.upper(), key=open(normpath(join(BASE_DIR, 'settings/secrets/secret_key'))).read().strip()),
    'export {site}_PSQL_PASS=\'{pword}\''.format(site=SITE_NAME.upper(), pword=open(normpath(join(BASE_DIR, 'settings/secrets/psql_pass'))).read().strip()),
]
########## END GLOBALS


########## DEPLOY AND SERVE
@task
def deploy(branch=None):
    """Get the latest code from git, and install reqs from reqs/prod.txt"""

    if branch:
        run('git remote update')
        with settings(warn_only=True):
             # if the branch doesn't exist locally yet - this may fail without crashing the script
            run('git checkout -t %s' % branch)
        # If the branch is here locally, this will check it out. If it's not, we checked it out above - this will just do it again.
        run('git checkout %s' % branch)
        run('git pull origin %s' % branch)
    else:
        run('git pull origin master')  # specificity never hurt anybody

    run('pip -q install -r reqs/prod.txt')

@task
def start():
    """Serve the app using supervisord"""
    # check to make sure logs dir exists, make it if not
    if not exists("logs"):
        run('mkdir logs')

    run('python manage.py supervisor --daemon')

@task
def stop():
    """Kill supervisord"""
    with open('/tmp/supervisor_{}.pid'.format(SITE_NAME),'r') as f:
        pid = f.read()
        run('kill -15 ' + pid)  # SIGTERM is what supervisord expects to gracefully shut down workers

@task
def restart():
    """Restart Gunicorn and Celery via supervisord."""
    stop()
    start()

@task
def tail():
    """Follow the logs of the supervisord processes."""
    run('tail -f logs/{}.log'.format(SITE_NAME))

######### END DEPLOY AND SERVE


########## DATABASE MANAGEMENT
@task
def syncdb():
    """Run a syncdb"""
    run('%(run)s syncdb --noinput' % env)

@task
def migrate(app=None):
    """Apply one (or more) migrations. If no app is specified, fabric will
    attempt to run a site-wide migration.

    :param str app: Django app name to migrate.
    """
    if app:
        run('%s migrate %s --noinput' % (env.run, app))
    else:
        run('%(run)s migrate --noinput' % env)
########## END DATABASE MANAGEMENT


########## FILE MANAGEMENT
@task
def collectstatic():
    """Collect all static files, and copy them to S3 for production usage."""
    run('%(run)s fasts3collectstatic' % env)
########## END FILE MANAGEMENT


@task
def reqs():
    """Install system packages not included on standard Debian installs"""
    packages = [
        'libevent-dev',
        'libsasl2-dev',
        'postgresql postgresql-contrib libpq-dev',
        'rabbitmq-server',
    ]

    # make sure nothing ever asks for input
    run('export DEBIAN_FRONTEND=noninteractive')

    for package in packages:
        sudo('apt-get -y install ' + package)

    # put the frontend back
    run('export DEBIAN_FRONTEND=dialog')


@task
def virtualize():
    """Create a virtualenv for python packages"""
    if not exists("/home/bjacobel/.virtualenvs/" + SITE_NAME):
        run('virtualenv /home/bjacobel/.virtualenvs/' + SITE_NAME)
    else:
        print("Virtualenv already exists.")


@task
def postgres():
    """Setup Postgres with a new user; set passwords and permissions"""
    run('psql -c "CREATE ROLE {} WITH LOGIN;"'.format(SITE_NAME))
    run('psql -c "ALTER ROLE {role} WITH PASSWORD \'{pword}\';"'.format(role=SITE_NAME, pword=os.environ.get('{}_PSQL_PASS'.format(SITE_NAME.upper()))))
    run('psql -c "CREATE DATABASE {};"'.format(SITE_NAME))


@task
def env_check():
    """Make sure the environment is what we think it is."""
    run("printenv | grep {}".format(SITE_NAME.upper()))


@task
def setup():
    """Meta-task - should take a machine from bare to ready to start()"""
    reqs()
    postgres()
    virtualize()
    deploy()
    syncdb()
    migrate()
    collectstatic()