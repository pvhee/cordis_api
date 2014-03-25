# Cordis API
**Django REST server for retrieving structured Cordis project information**

## Run Django

Activate the virtual environment

     source venv/bin/activate

Run the webserver

	venv/bin/python manage.py runserver

## Removing the local cache

Projects are stored in the local cache for performance improvements.

To clear the local cache on Heroku, you can do

	heroku pg:psql
	TRUNCATE cordis_project;

and check that all is empty with

	SELECT count(*) FROM cordis_project;

## Credits
 
* http://openconsortium.eu
* Development by @pvhee from @marzeelabs, http://marzeelabs.org


