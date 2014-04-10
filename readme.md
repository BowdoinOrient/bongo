###bongo
#####(a.k.a. BONUS 3.0)
---
bongo is the third version of the Bowdoin Orient Network Update System. It is based on Django, hence the weird name.

####setup:
You'll need:
- Python 2.7 
- Postgres ([Postgres.app](http://postgresapp.com) is a good option if you're on OS X).
- [Yuglify](https://github.com/yui/yuglify): `npm -g install yuglify`

1. Run the following commands in psql or [PG Commander](https://eggerapps.at/pgcommander/) to set up Postgres:
        
        CREATE ROLE bongo WITH LOGIN CREATEDB PASSWORD 'bongo';
        CREATE DATABASE bongo;

2. Then you'll need to run:

        pip install -r reqs/dev.txt
        python manage.py syncdb
        python manage.py test
        python manage.py collectstatic
        python manage.py runserver

####deployment:
Deployment is handled via Fabric. `fab ?` will show you all the available commands. `fab setup` should take you from a blank Ubuntu or Debian install to ready to deploy, then you can `fab deploy` and `fab start`.

####tests:  [![Build Status](https://travis-ci.org/BowdoinOrient/bongo.svg)](https://travis-ci.org/BowdoinOrient/bongo) [![Coverage Status](https://coveralls.io/repos/BowdoinOrient/bongo/badge.png)](https://coveralls.io/r/BowdoinOrient/bongo)

