findhelp
========

A platform to help

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style
.. image:: https://travis-ci.com/yusufhilmi/findhelp.svg?branch=master
     :target: https://travis-ci.com/yusufhilmi/findhelp
     :alt: CI status by Travis CI
.. image:: https://img.shields.io/badge/License-MIT-green.svg
     :target: https://github.com/yusufhilmi/findhelp/blob/master/LICENSE
     :alt: MIT LICENSE


Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.


Translations
^^^^^^^^^^^^^

To translate to a certain language use the following commands. Commands below shows how to compile to Turkish::

    $ docker-compose -f local.yml run --rm django python manage.py makemessages -l tr

Before compilation make sure you have translated locale/tr/LC_MESSAGES/django.po file, then run::

    $ docker-compose -f local.yml run --rm django python manage.py compilemessages


Running tests with py.test
^^^^^^^^^^^^^^^^^^^^^^^^^^

::

  $ docker-compose -f local.yml run --rm django pytest


Email Server
^^^^^^^^^^^^

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server `MailHog`_ with a web interface is available as docker container.

Container mailhog will start automatically when you will run all docker containers.

With MailHog running, to view messages that are sent by your application, open your browser and go to ``http://127.0.0.1:8025``

.. _mailhog: https://github.com/mailhog/MailHog


Custom Bootstrap Compilation
^^^^^^

The generated CSS is set up with automatic Bootstrap recompilation with variables of your choice.
Bootstrap v4 is installed using npm and customised by tweaking your variables in ``static/sass/custom_bootstrap_vars``.

You can find a list of available variables `in the bootstrap source`_, or get explanations on them in the `Bootstrap docs`_.


Bootstrap's javascript as well as its dependencies is concatenated into a single file: ``static/js/vendors.js``.


.. _in the bootstrap source: https://github.com/twbs/bootstrap/blob/v4-dev/scss/_variables.scss
.. _Bootstrap docs: https://getbootstrap.com/docs/4.1/getting-started/theming/


PRODUCTION SETTINGS
^^^^^^^^^^^^^^^^^^^

to-do