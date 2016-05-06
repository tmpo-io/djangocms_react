Tempo Django CMS with Cookiecutter
============================

A [Cookiecutter](https://github.com/audreyr/cookiecutter) template for [DjnagoCMS](https://www.django-cms.org/) and frontend tools: [Gulp](https://github.com/gulpjs/gulp), [Sass](https://github.com/sass/sass), [Backbone](https://github.com/jashkenas/backbone)


Installation and usage
----------------------

If you want to create a personal website using Django CMS with [tmpo.io](https://tmpo.io) preconfiguration.

First, get cookiecutter::

    $ pip install cookiecutter

Now run it against this repo::

    $ cookiecutter git@github.com:tmpo-io/djangocms_base.git

You'll be prompted for some questions:

- Repo project url
- Project name
- Languages you want to setup

Setting up the project
----------------------

Let's create a virtualenv inside the project dir if you aren't working with Docker

    $ virtualenv env 

Now your virtualenv is created you sould activate in order to install the project requirements

    $ source env/bin/activate
    $ pip install -r src/requirements.txt

We are working with specific settings for each environment (dev / prod)

    $ echo 'dev' > environment

We need to sync the DB, let's migrate and run the server

    $ src/manage.py migrate

Add a new superuser

    $ src/manage.py createsuperuser admin

Now you are ready to use Django CMS! with tmpo.io configuration.

    $ src/manage.py runserver

Docker support
--------------

If you want to run it with Docker you can find an embedded docker image (src/Dockerfile), to run Gunicorn.


