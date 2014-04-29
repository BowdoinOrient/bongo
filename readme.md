###bongo
---
Bongo is the third version of the Bowdoin Orient Network Update System. Previous versions of BONUS have integrated the Orient's front-facing website and CMS in one environment. Bongo instead plans to provide only a CMS and API for a future front-facing website to hook into.

####setup:
You'll need:
- Python 2.7 (Why? mostly because Fabric doesn't support Python 3.)
- Postgres ([Postgres.app](http://postgresapp.com) is a good option if you're on OS X).

1. Run the following commands in psql or [PG Commander](https://eggerapps.at/pgcommander/) to set up Postgres:
        
        CREATE ROLE bongo WITH LOGIN CREATEDB PASSWORD 'bongo';
        CREATE DATABASE bongo;

2. Then you'll need to run:

        pip install -r reqs/dev.txt
        python manage.py makemigrations bongo
        python manage.py migrate
        python manage.py collectstatic
        python manage.py runserver

3. `bongo/settings/secrets` is a directory designed for application secrets, keys, and passwords. It should contain several files, each containing the following information on a single line:
    - `postgres_pass`: a password for the `bongo` postgres role in production
    - `secret_key`: the [Django secret key](https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-SECRET_KEY) for the production installation
    - `aws_id`: The ID key for the AWS/S3 account bongo static files are hosted on
    - `aws_secret_key`: The secret key for the AWS/S3 account bongo static files are hosted on

####deployment:
Deployment is handled via Fabric. `fab ?` will show you all the available commands. `fab setup` should take you from a blank Ubuntu or Debian install to ready to deploy, then you can `fab deploy` and `fab start`.

####tests:  [![Build Status](https://travis-ci.org/BowdoinOrient/bongo.svg)](https://travis-ci.org/BowdoinOrient/bongo) [![Coverage Status](https://coveralls.io/repos/BowdoinOrient/bongo/badge.png)](https://coveralls.io/r/BowdoinOrient/bongo)

