###bongo
---
Bongo is the third version of the Bowdoin Orient Network Update System. Previous versions of BONUS have integrated the Orient's front-facing website and CMS in one environment. Bongo instead plans to provide only a CMS and API for a future front-facing website to hook into.

####setup:
You'll need:
- Python 2.7 or 3.4
- Postgres ([Postgres.app](http://postgresapp.com) is a good option if you're on OS X).
- NPM and Bower

1. Run the following commands in psql or [PG Commander](https://eggerapps.at/pgcommander/) to set up Postgres:

        CREATE ROLE bongo WITH LOGIN CREATEDB PASSWORD 'bongo';
        CREATE DATABASE bongo;

2. Then you'll need to run:

        pip install -r reqs/dev.txt
        python manage.py makemigrations bongo
        python manage.py migrate
        python manage.py bower install
        python manage.py collectstatic
        python manage.py gruntserver

3. `bongo/settings/secrets` is a directory designed for application secrets, keys, and passwords. It should contain several files, each containing the following information on a single line:
    - `postgres_pass`: a password for the `bongo` postgres role in production
    - `secret_key`: the [Django secret key](https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-SECRET_KEY) for the production installation
    - `aws_id`: The ID key for the AWS/S3 account bongo static files are hosted on
    - `aws_secret_key`: The secret key for the AWS/S3 account bongo static files are hosted on

####deployment:
Deployment is currently handled via Fabric. Because Fabric doesn't and won't support Python 3, you must deploy from Python 2.

Useful commands include:
- `fab deploy`, which will update the git repo and virtualenv on the production server. Deploy a specific branch with `fab deploy:<branch>`.
- `fab start/fab stop`, which run and kill the server,
- `fab restart`, which is an alias for the above two, and
- `fab managepy`, which lets you run an arbitrary `python manage.py` command in production. For instance, `fab managepy:migrate` will run deployed database migrations.

Replacement of Fabric with Ansible is planned so that Bongo will be fully Python 3 compatible, so don't get too attached to it.

####tests:  
You can run Bongo's test suite with `python manage.py test`. The current build status is:

[![Build Status](https://img.shields.io/travis/BowdoinOrient/bongo/develop.svg?style=flat)](https://travis-ci.org/BowdoinOrient/bongo) [![Coverage Status](https://img.shields.io/coveralls/BowdoinOrient/bongo/develop.svg?style=flat)](https://coveralls.io/r/BowdoinOrient/bongo?branch=develop)


####using the api
Bongo is a fairly typical RESTful API.

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

`GET /api/v1/post/?ordering=-published`

Some endpoints allow you to cross-reference resources. For example, to return a  list of all of the posts in a particular section:

        GET /api/v1/section/3/posts
