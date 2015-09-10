###Bongo
[![Build Status](https://img.shields.io/travis/BowdoinOrient/bongo/develop.svg?style=flat)](https://travis-ci.org/BowdoinOrient/bongo) [![Coverage Status](https://img.shields.io/coveralls/BowdoinOrient/bongo/develop.svg?style=flat)](https://coveralls.io/r/BowdoinOrient/bongo?branch=develop)  [![Stories in Progress](https://badge.waffle.io/BowdoinOrient/bongo.svg?label=In%20Progress&title=In%20Progress)](http://waffle.io/BowdoinOrient/bongo)
---
Bongo is the third version of the Bowdoin Orient Network Update System. The project's goal is to provide a professional, scalable and modern platform on which readers, editors and contributors of the Bowdoin Orient can read and write Bowdoin's news for the next decade. In addition, Bongo hopes to be a platform that can be reused and remixed to meet the needs of other journalistic organizations.

####Contributing
Bongo is using [waffle.io](http://waffle.io/BowdoinOrient/bongo) for project management. If you're interested in contributing code to Bongo, check out the scrum board and see what's in the backlog. Most stories should already be pointed, prioritized and given acceptance criteria. If you're interested in a story that's missing one of those, or have any other questions, email [Brian](mailto:bjacobel@gmail.com) - he can help match up your skills with the Orient's needs.


####Setup
You'll need:

- Python >=3.4
- NodeJS >= 0.10
- Postgres ([Postgres.app](http://postgresapp.com) is a good option if you're on OS X, `brew`'s postgres package always gives me issues).
- Redis >= 2.8 (if you plan to contribute to scheduled task-related functionality)
- Vagrant (if you plan to contribute to the project's Ansible playbook)
- MySQL/MariaDB (if you plan to contribute changes to the project's adapter to the 2002-2015 database)

Note that while all current development is being done with Python 3.4, the code base should support Python 2.7 if you are for some reason unable to upgrade.

1. Install [Homebrew](https://brew.sh).

2. Install required system-level dependencies

        brew install python3 node

	Include `postgres` in the above if you choose not to use [Postgres.app](http://postgresapp.com).

3. Install optional system-level dependencies (based on "If you plan to..." above)

        brew install redis vagrant mariadb


4. Run the following commands in `psql` or [Postico](https://eggerapps.at/postico/) to set up the Postgres database:

        CREATE ROLE bongo WITH LOGIN CREATEDB PASSWORD 'bongo';
        CREATE DATABASE bongo;

5. Install Python dependencies with:

        pip install -r reqs/dev.txt

	It's recommended to do this step inside of a Python [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) if you do any other Python development on this machine.

6. Obtain a copy of the `ansible/env_vars/secure.yml` file. It contains application secrets and third-party API credentials. An example file with secrets ommitted is at `ansible/env_vars/secure_safe.yml`. You may commit changes to this file to the repository, but please ensure you do not commit the actual secrets file.

7. Set up the database with:

        python manage.py syncdb

8. Check that setup was successful with:

        python manage.py check

####Deployment
The code base includes Ansible roles for configuring a Linux server and deploying Bongo onto it.

The following command will execute the complete playbook on all of the hosts defined in `ansible/inventory/prod`:

    ansible-playbook ansible/deploy.yml

To save time during development, it is not neccesary to run the complete playbook - many plays only need to be executed once per host. Most changes to the Django application can be deployed with the following playbook subset:

    ansible-playbook ansible/deploy.yml --tags="web"

If you are contributing changes to the Ansible playbook, you may use the included Vagrantfile to provision a test VM that approximates the production server. To deploy Bongo to Vagrant, run the following:

    vagrant up
    ansible-playbook -i ansible/inventory/vagrant.yml ansible/deploy.yml
    sudo echo "192.168.100.100 bowdoinorient.local" >> /etc/hosts

and visit [http://bowdoinorient.local](http://bowdoinorient.local) in your browser if the deploy is successful.

Bongo is currently deployed at [bowdoinorient.co](http://bowdoinorient.co).

####Tests
You can run Bongo's test suite with `python manage.py test` (and should, often!). The current build status and test coverage stats are shown at the top of this readme. Pull requests should include tests to maintain or increase the current code coverage percentage.


The test suite currently runs against both Python 2.7 and 3.4. so please ensure all pull requests are backwards-compatible (or forwards-, if developed with 2.7).


####Using the API
Bongo includes a JSON API acessible at [<base_url>/api/v1](https://bowdoinorient.bjacobel.com/api/v1). Its structure is fairly standard REST.

To obtain a list of all resources of a type:

        GET /api/v1/<resource>

To obtain details about a specific instance of a resource type:

        GET /api/v1/<resource>/<#>

The object detail endpoint offers more method options to authenticated users:

        POST/PUT/DELETE/UPDATE /api/v1/<resource>/<#>

Authentication methods are still being developed.

Every endpoint accepts two query parameters.

1. `limit=<n>` limits the response to a maximum of `n` objects. Subsequent object are accessible through pagination. The default limit is 25, and the maximum is 100.

2. `ordering=<criteria>` orders the response objects by `criteria`, where `criteria` is a field on the contained objects Django knows how to order. This argument accepts a `-` prefix for reverse ordering. For example, to return a list of posts in reverse chronological order:

        GET /api/v1/post/?ordering=-published

Some endpoints allow you to cross-reference resources. For example, to return a  list of all of the posts in a particular section:

        GET /api/v1/section/3/posts


#### License
Bongo is released under the MIT license. If you have questions about using Bongo for your organization, please [get in touch](mailto:bjacobel@gmail.com).
