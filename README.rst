Behind the curtain
==================
Code examples for the talk `"Behind the curtain - How Django handles a request" <https://2018.djangocontent.eu/hd/talk/37A8EC/>`_ at DjangoCon Europe 2018.

Each sub-directory contains a small Django project.

default
  A project with default structure and settings, generated with ``django-admin.py startproject default``

simple
  A really simple project

middleware
  Like ``simple``, but with three middleware classess that do nothing

Usage
-----

The only external dependency is Django 2.0.x, meaning you have to use Python 3.4 or higher.

There is a ``requirements.txt`` file::

    (venv) $ pip install -r requirements.txt

You can the change into one of the project directories and run the ``server.py`` script, which starts a server on ``127.0.0.1:8000``::

    (venv) $ cd simple
    (venv) $ python server.py

Note that the server exits after handling a single request.
