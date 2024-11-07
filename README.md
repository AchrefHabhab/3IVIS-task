# Working Student Django Developer Assignement - 3IVIS

Welcome to the data engineering student assignment for 3IVIS!

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

License: MIT

## Settings

Cookiecutter django [settings](https://cookiecutter-django.readthedocs.io/en/latest/1-getting-started/settings.html).

D3 [documentation](https://d3js.org/)

## Intallation

### install CookieCutter


- To install **Cookiecutter**, use this command:

      $ pip install cookiecutter

### Generate the Project:

- Create and run the environment:

        $ python -m venv .venv
        $ .\.venv\Scripts\activate

### Install Dependencies

-Run the following commands to install the required dependencies:

    $ pip install -r requirements/local.txt
    $ pip install Django djangorestframework django-nvd3
    $ nvm install node
    $ nvm use node
    $ npm install d3

### Create a migration and migrate

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Create a migration and migrate:

- don't forget to change the database URL:
    
        $ DATABASES = {
            "default": env.db(
            "DATABASE_URL",
            default="postgres://postgres:root@127.0.0.1:5432/my_awesome_project",
            ),  
        }
        
        $ python manage.py makemigrations
        $ python manage.py migrate

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

## create an app for handling charts 

    $ cd task
    $ python ../manage.py startapp charts

## run app 
    $ python manage.py runserver
