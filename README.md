# Radio in a Box #

_Radio in a Box_ is an experiment in radio that's near by, perhaps next door. It uses [Django](https://www.djangoproject.com/), [Pinax](http://pinaxproject.com/), and [Bootstrap](http://twitter.github.com/bootstrap/).

### Installation and getting started ###

#### Create a virtual environment (recommended)

Follow the documentation at [virtualenv](http://www.virtualenv.org/) or [virtualenvwrapper](http://pypi.python.org/pypi/virtualenvwrapper). If you're using virtualenvwrapper, then create a new virtual environment with

    $ mkvirtualenv radioradio --no-site-packages
	$ activate radioradio

#### Checkout the project

    $ git clone git://github.com/gerlad/radio-in-a-box.git

#### Install all project requirements (Django, Pinax, Bootstrap, etc.):

    $ cd radioradio
    $ pip install -r requirements/project.txt

#### Install PostgreSQL/PostGIS and geographic libaries

    $ sudo apt-get install binutils python-setuptools postgresql-8.4-postgis postgresql-server-dev-8.4 python-psycopg2 gdal-bin python-gdal libproj-dev

#### [NOTE: If you're developing on Mac OSX Lion read this for postgres]: 
	http://www.jonathandean.com/2011/08/postgresql-8-4-on-mac-os-x-10-7-lion
		
#### Create PostGIS template

...on Ubuntu 10.10 with PostGIS 1.5 for instance:

    $ sudo su postgres
    $ POSTGIS_SQL_PATH=/usr/share/postgresql/8.4/contrib/postgis-1.5
    $ createdb -E UTF8 template_postgis
    $ createlang -d template_postgis plpgsql
    $ psql -d postgres -c "UPDATE pg_database SET datistemplate='true' WHERE datname='template_postgis';"
    $ psql -d postgres -c "update pg_database set datistemplate = false where datname = 'template_postgis';"
    $ psql -d template_postgis -f $POSTGIS_SQL_PATH/postgis.sql
    $ psql -d template_postgis -f $POSTGIS_SQL_PATH/spatial_ref_sys.sql
    $ psql -d template_postgis -c "GRANT ALL ON geometry_columns TO PUBLIC;"
    $ psql -d template_postgis -c "GRANT ALL ON spatial_ref_sys TO PUBLIC;"
    $ psql -d template_postgis -c "GRANT ALL ON geography_columns TO PUBLIC;"

Please see [GeoDjango installation docs](https://docs.djangoproject.com/en/1.3/ref/contrib/gis/install/) for more detailed information and troubleshooting.

#### Create radioradio database user

    $ createuser radioradio
    $ #Shall the new role be a superuser? (y/n) n
    $ #Shall the new role be allowed to create databases? (y/n) y
    $ #Shall the new role be allowed to create more new roles? (y/n) n
    $ psql
    $ ALTER ROLE radioradio WITH password 'password';
    $ \q
    $ exit

#### Create new user radioradio

    $ sudo adduser radioradio
	
#### Create radioradio database

    $ sudo su - radioradio
    $ createdb radioradio -T template_postgis

#### Add your database configuration

    DATABASES = {
	    "default": {
	        "ENGINE": "django.contrib.gis.db.backends.postgis",
	        "NAME": "radioradio",
	        "USER": "radioradio",
	        "PASSWORD": "password",
	        "HOST": "",
	        "PORT": "",
	    }
	}

.. to `settings.py` or create a `local_settings.py` (recommended)

#### Syncronize database and run the development server

    $ python manage.py syncdb
    $ python manage.py runserver


#### Test the application

...in your localhost at [http://127.0.0.1:8000](http://127.0.0.1:8000)

