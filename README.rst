Behind the curtain
==================
Code examples for the workshop "Behind the curtain - How Django handles a request", presented at `DjangoCon Europe 2019 <https://members.2019.djangocon.eu/conference/talk/UH9AKN/>`_ (`Slides <https://members.2019.djangocon.eu/media/behind_the_curtain_djangocon_europe_2019.pdf>`_).

Each sub-directory contains a small Django project.

default
  A project with default structure and settings, generated with ``django-admin.py startproject default``

simple
  A really simple project

middleware
  Like ``simple``, but with three middleware classes that do some logging.

Usage
-----

The only external dependency is Django 2.2.x, meaning you have to use Python 3.5 or higher.

There is a ``requirements.txt`` file::

    (venv) $ pip install -r requirements.txt

You can the change into one of the project directories and run the ``server.py`` script, which starts a server on ``127.0.0.1:8000``::

    (venv) $ cd simple
    (venv) $ python server.py

Note that the server intentionally exits after handling a single request.
