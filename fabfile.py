from fabric.api import env, run, local, task, prefix, cd, sudo, settings
from fabric.context_managers import shell_env
from fabric.contrib.files import exists
from fabric.colors import red, green, blue
from bongo.settings.common import BASE_DIR
from os.path import join, normpath
import fabtools
import time

def shellquote(s):
    return "'" + s.replace("'", "'\\''") + "'"

envr = {
    "DJANGO_SETTINGS_MODULE" : "bongo.settings.prod",
    "BONGO_SECRET_KEY" : shellquote(open(normpath(join(BASE_DIR, 'settings/secrets/secret_key'))).read().strip()),
    "BONGO_POSTGRES_PASS" : shellquote(open(normpath(join(BASE_DIR, 'settings/secrets/postgres_pass'))).read().strip()),
    "AWS_ACCESS_KEY_ID" : shellquote(open(normpath(join(BASE_DIR, 'settings/secrets/aws_id'))).read().strip()),
    "AWS_SECRET_ACCESS_KEY" : shellquote(open(normpath(join(BASE_DIR, 'settings/secrets/aws_secret_key'))).read().strip()),
    "BONGO_RAVEN_DSN" : shellquote(open(normpath(join(BASE_DIR, 'settings/secrets/raven_dsn'))).read().strip()),
    "BONGO_LOGENTRIES_TOKEN" : shellquote(open(normpath(join(BASE_DIR, 'settings/secrets/logentries_token'))).read().strip()),
    "DISQUS_API_KEY" : shellquote(open(normpath(join(BASE_DIR, 'settings/secrets/disqus_api_key'))).read().strip()),
    "SCRIBD_API_KEY" : shellquote(open(normpath(join(BASE_DIR, 'settings/secrets/scribd_api_key'))).read().strip()),
}

prefix_string = ""

for key, value in envr.iteritems():
    prefix_string += "export {}={} && ".format(key, value)

prefix_string = prefix_string[:-4]

########## GLOBALS
env.run = 'python manage.py'
env.user = 'orient'
env.hosts = ['citadel.bjacobel.com']
########## END GLOBALS

######################
# Note: I highly reccommend you log into orient@ each of env.hosts and add your id_rsa.pub to ~/.ssh/authorized_keys,
# it will make using Fabric much easier.
######################


########## DEPLOY

@task
def deploy(branch=None):
    """Get the latest code from git, and install reqs from reqs/prod.txt"""

    if branch is None:
        branch = local("git rev-parse --abbrev-ref HEAD")

    local("git push origin " + branch)

    with cd("/home/orient"):
        fabtools.require.git.working_copy("git@github.com:bowdoinorient/bongo.git", branch=branch)

        with fabtools.python.virtualenv('/home/orient/.virtualenvs/bongo'):
            with cd("/home/orient/bongo"):
                run('pip -q install -r reqs/prod.txt')

                with prefix(prefix_string):
                    run('%(run)s s3collectstatic --noinput' % env)
                    run('%(run)s compress' % env)

############ END DEPLOY


######### SERVE AND RESTART

@task
def start():

    """Serve the app using supervisord"""

    with cd("/home/orient/bongo"):
        with fabtools.python.virtualenv('/home/orient/.virtualenvs/bongo'):
            with prefix(prefix_string):
                # check to make sure logs dir exists, make it if not
                if not exists('/home/orient/bongo/logs'):
                    run('mkdir logs')

                run('supervisord')

@task
def stop():

    """Kill supervisord"""

    pid = run('cat /tmp/supervisor_bongo.pid')
    run('kill -15 ' + pid)  # SIGTERM is what supervisord expects to gracefully shut down workers

@task
def restart():

    """Restart Gunicorn and Celery via supervisord."""

    stop()
    time.sleep(5)  # supervisor takes a couple of seconds to gracefully stop
    start()

@task
def tail():

    """Follow the logs of the supervisord processes."""

    with cd("/home/orient/bongo"):
        run('tail -f logs/bongo.log')

######### END SERVE AND RESTART


########## DATABASE MANAGEMENT
@task
def syncdb():

    """Run a syncdb"""

    with cd("/home/orient/bongo"):
        with fabtools.python.virtualenv('/home/orient/.virtualenvs/bongo'):
            with prefix(prefix_string):
                run('%(run)s syncdb --noinput' % env)

########## END DATABASE MANAGEMENT


########## FILE MANAGEMENT
@task
def collectstatic():

    """Collect all static files, and copy them to S3 for production usage."""

    with cd("/home/orient/bongo"):
        with fabtools.python.virtualenv('/home/orient/.virtualenvs/bongo'):
            with prefix(prefix_string):
                run('%(run)s fasts3collectstatic --noinput' % env)
########## END FILE MANAGEMENT


####### BUILD THE ENVIRONMENT

@task
def setup():
    """Take a vanilla Debian/Ubuntu machine and get it ready to deploy onto"""

    # make sure nothing ever asks for input
    with shell_env(DEBIAN_FRONTEND='noninteractive'):

        sudo('apt-get -qq update')
        sudo('apt-get -qq upgrade')

        # Install system packages not included on standard Debian installs
        packages = [
            'libevent-dev',
            'libmemcached-dev',
            'postgresql postgresql-contrib',
            'rabbitmq-server',
            'nginx',
            'git',
        ]

        for package in packages:
            sudo('apt-get -q -y install ' + package)

    # Create a virtualenv
    run('pip install virtualenv')

    if not exists('/home/orient/.virtualenvs/bongo'):
        run('mkdir -p /home/orient/.virtualenvs/bongo')
        run('virtualenv -p /usr/local/bin/python3 /home/orient/.virtualenvs/bongo')

    print(red("Create a password for the postgres account."))
    sudo('passwd postgres')

    # Setup Postgres with a new user; give access to database
    with settings(sudo_user="postgres", warn_only=True):
        sudo('psql -c "CREATE ROLE bongo WITH LOGIN PASSWORD \'{}\';"'.format(envr['BONGO_POSTGRES_PASS']))
        sudo('psql -c "CREATE DATABASE bongo;"')

    # fire up nginx
    sudo('nginx')

    print(green("Server setup successfully. Now run ") + blue("fab deploy."))
    print(red("Note: ")+"the server has NOT been secured. Do not neglect to set up a firewall,")
    print("iptables, fail2ban, and SSH key-only login you WILL get the Orient pwned.")

########### END BUILD THE ENVIRONMENT

@task
def managepy(command):
    """run an arbitrary 'python manage.py' command"""

    with cd("/home/orient/bongo"):
        with fabtools.python.virtualenv('/home/orient/.virtualenvs/bongo'):
            with prefix(prefix_string):
                run(env.run +" "+ command)

@task
def command():
    """print the prefix string needed to run commands manually over SSH"""
    local("echo '{} &&' | pbcopy".format(prefix_string))
