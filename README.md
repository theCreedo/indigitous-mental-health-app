## Local Development
It is highly recommended to use a virtualenv to manage dependencies.
1. Create a PostgreSQL database named `mhealth`
2. Run `virtualenv venv` to create a virtual environment for the project
3. Run `source venv/bin/activate`
2. Run `pip install -r requirements.txt`
3. Create a `.env` file with your configuration like the following:
```
LOG_LEVEL=debug
SERVICE_NAME=mhealth
DEBUG=True
DATABASE_URL='postgresql://INSERT_YOUR_USERNAME@127.0.0.1:5432/mhealth'
NONCE_SECRET='another secret here'
HASHIDS_SALT='ur salt here'
SECRET_KEY='a0th3rS3cr3tH3r3'
BASE_URL='http://localhost:5000'
GENERAL_INFO_EMAIL='INSERT_EMAIL_HERE'
CDN_URL=''
REDISTOGO_URL='127.0.0.1:6379'
```
4. Making sure PostgreSQL is running, set up the tables by running `python manage.py db upgrade`
5. Run the server by running `python manage.py runserver`


## Inspiration


## What it does


## How we built it
We used Flask for the backend to handle all processes and communicate with our database - Postgresql. We used basic Bootstrap, HTML, CSS, and JavaScript in order to display our website.

## Challenges we ran into


## Accomplishments that we're proud of


## What we learned


## What's next for Mhealth
