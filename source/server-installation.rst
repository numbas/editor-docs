Installing an editor server
===========================

Running a personal instance of the editor 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Windows
-------

Installation
************

#. Install Python 3 and Python 2.7 from `python.org/download <http://python.org/download>`_. Python 2 is needed to run the webserver, while Python 3 is needed to run the Numbas tools.
#. Download and install `setuptools for Python 2 <http://pypi.python.org/pypi/setuptools>`_.
#. Run::

    c:\python27\Scripts\easy_install pip

#. Either `download the Numbas runtime tools from github <https://github.com/numbas/Numbas/archive/master.zip>`_ and extract to a folder called numbas_runtime, or git clone the repository::

    git clone git://github.com/numbas/Numbas.git numbas_runtime

#. Either download the Numbas editor from github and extract to a folder called numbas_editor, or git-clone the repository::

    git clone git://github.com/numbas/editor.git numbas_editor

#. Go into the editor directory, and install all the required Python2 modules::

    c:\python27\Scripts\pip install -r requirements.pip

Configuration
*************

#. Copy :file:`numbas/settings.py.dist` to :file:`numbas/settings.py`
#. Change ``STATIC_ROOT`` to ``'editor/static'``
#. Change ``NUMBAS_PATH`` to ``'../numbas_runtime'``
#. Change ``PREVIEW_PATH`` to ``'editor/static/previews'``, and create that directory.
#. Change ``PREVIEW_URL`` to ``'/static/previews/'``
#. Change ``PYTHON_EXEC`` to ``'c:/python33/python'``
#. Copy :file:`numbas/database.py.dist` to :file:`numbas/database.py`
    #. Change ``ENGINE`` to ``'django.db.backends.sqlite3'``
    #. Change ``NAME`` to ``'database.sqlite'``
#. Sync the database:
    #. ``c:\python27\python manage.py syncdb``
    #. Create a superuser (answer ``yes``)
    #. Enter username, e-mail address, and password
#. Copy :file:`editor/templates/index.html.dist` to :file:`editor/templates/index.html`.
#. Start the server::

    c:\python27\python manage.py runserver

#. Open http://localhost:8000

Mac
---

Installation
************

#. Install Python 3 and Python 2.7 from `python.org/download <http://python.org/download>`_. Python 2 is needed to run the webserver, while Python 3 is needed to run the Numbas tools.
#. Download and install `setuptools for Python 2 <http://pypi.python.org/pypi/setuptools>`_.
#. Run::

    easy_install pip

#. Either `download the Numbas runtime tools from github <https://github.com/numbas/Numbas/archive/master.zip>`_ and extract to a folder called numbas_runtime, or git clone the repository::

    git clone git://github.com/numbas/Numbas.git numbas_runtime

#. Either download the Numbas editor from github and extract to a folder called numbas_editor, or git-clone the repository::

    git clone git://github.com/numbas/editor.git numbas_editor

#. Go into the editor directory, and install all the required Python2 modules::

    pip install -r requirements.pip

Configuration
*************

#. Copy :file:`numbas/settings.py.dist` to :file:`numbas/settings.py`
#. Change ``STATIC_ROOT`` to ``'editor/static'``
#. Change ``NUMBAS_PATH`` to ``'../numbas_runtime'``
#. Change ``PREVIEW_PATH`` to ``'editor/static/previews'``, and create that directory.
#. Change ``PREVIEW_URL`` to ``'/static/previews/'``
#. Change ``PYTHON_EXEC`` to ``'python3'``
#. Copy :file:`numbas/database.py.dist` to :file:`numbas/database.py`
    #. Change ``ENGINE`` to ``'django.db.backends.sqlite3'``
    #. Change ``NAME`` to ``'database.sqlite'``
#. Sync the database:
    #. ``python2 manage.py syncdb``
    #. Create a superuser (answer ``yes``)
    #. Enter username, e-mail address, and password
#. Copy :file:`editor/templates/index.html.dist` to :file:`editor/templates/index.html`.
#. Start the server::

    python2 manage.py runserver
#. Open http://localhost:8000


Installing a shared server
^^^^^^^^^^^^^^^^^^^^^^^^^^

Outline instructions on setting up the Numbas editor with a backend MySQL database. The following is for an Ubuntu Precise (12.04) Linux server.

Essential package installation
------------------------------

Packages that would be installed as part of a standard Ubuntu install are not listed. Python 3 is required for compilation of Numbas exams; Python 2.6 (or greater) is required for Django.

Install Apache, Git, Apache WSGI module, MySQL, Python 3, and the Python Imaging Library using the packaging system::

    apt-get install apache2 git-core libapache2-mod-wsgi mysql-server mysql-common python3 python-imaging 
    
Virtualenv
**********

Rather than rely on the packaged version of Django, a more flexible approach is to use `virtualenv http://www.virtualenv.org/>`, which is a tool to create an isolated Python environment.

#. Install Pip::

    apt-get install python-pip

#. Install virtualenv::

    pip install virtualenv

#. Create the virtualenv in a suitable location::

    virtualenv /opt/python/numbas-editor
#. 
    Activate the virtualenv::

        /opt/python/numbas-editor/bin/activate 

    (this ensures that subsequent python packages are installed in this isolated environment, and not in the system environment).
#. Install extra packages to ensure Python packages compile and install correctly:: 

    apt-get install libmysqlclient-dev python-dev python-tk tcl-dev tk-dev

#. Install Django (need at least version 1.5) and other python dependencies of the editor (in the virtualenv)::

    pip install django django-taggit django-registration django-uuslug south MySQL-python

Configuration
-------------

#. Create database ``numbas_editor``
#. Create database user and grant privileges on ``numbas_editor`` database::

    grant all privileges on numbas_editor.* to 'numbas'@'localhost' identified by 'password';

#. Create Numbas directories outside the webroot::

    mkdir /srv/numbas /srv/numbas/dist /srv/numbas/media /srv/numbas/previews /srv/numbas/static

#. Set the correct ownership and permissions (need file system ACLs enabled on :file:`/srv`)::

    chmod 2770 media previews
    chmod 2750 dist static
    chgrp www-data dist media previews static
    setfacl -dR -m g::rwX media previews
    setfacl -dR -m g::rX dist static

#. Clone the Numbas repository::

    git clone git://github.com/numbas/Numbas /srv/numbas/dist

#. Create the editor directory and clone the editor under webroot::

    git clone git://github.com/numbas/editor /srv/www/numbas_editor

#. Copy the editor distribution database and settings files::

    cd /srv/www/numbas_editor/numbas
    cp database.py.dist database.py
    cp settings.py.dist settings.py

#. Edit :file:`database.py`:
    #. Set ``ENGINE`` to ``django.db.backends.mysql``
    #. Set ``NAME`` to the database name (``numbas_editor``)
    #. Set ``USER`` to the database user (``numbas``)
    #. Set ``PASSWORD`` to the database password (``password``)
#. Edit :file:`settings.py`:
    #. Make sure settings in ``GLOBAL_SETTINGS``, ``MEDIA_ROOT``, and ``STATIC_ROOT`` match those above.
    #. ``PREVIEW_URL`` should be set to the URL at which preview exams can be viewed (see the Apache 2 config file).
    #. ``PYTHON_EXEC`` is the path to the Python 3 executable.
#. Sync the database::

    cd /srv/www/numbas_editor
    python manage.py syncdb

#. Create a superuser (answer ``yes``)
#. Enter username, e-mail address, and password
#. Set up static files::

    python manage.py collectstatic --noinput

#. Copy :file:`editor/templates/index.html.dist` to :file:`editor/templates/index.html` and customise.
#. Copy :file:`web/django.wsgi.dist` to :file:`web/django.wsgi` and edit:
#. Make sure the ``sys.path.append`` line matches the path to the editor on the file system.
#. ``DJANGO_SETTINGS_MODULE`` should be set to ``numbas.settings`` (if following the above naming scheme).
#. Create apache config file and enable the site.
    #. Edit :file:`/etc/apache2/sites-available/numbas_editor` with contents similar to that in this example configuration file: :download:`apache2_ubuntu.conf <server-config/apache2_ubuntu.conf>`. If following these instructions exactly, then all that needs changing are the lines ``ServerName`` and ``ServerAdmin``.
    #. Run::
    
        a2ensite numbas_editor && service apache2 restart

#. Point a web browser at the server hosting the editor.

Self registration
-----------------
 
To allow users to register themselves within the editor, edit :file:`settings.py` and set ``ALLOW_REGISTRATION = True``. An e-mail is sent to the user, providing a link that they must click on to complete the registration process. To complete the self registration configuration do the following:

#. Set ``DEFAULT_FROM_EMAIL`` to something sensible. This is where the self-registration e-mails will appear to come from.
#. Log in to the admin interface of the editor (by going to ``http://server.domain/admin/``) as the admin user you created earlier. Click on :guilabel:`Sites`, then :guilabel:`example.com`, then change both fields to ``server.domain``. This sets the URL that will appear in the self-registration e-mails.

LDAP authentication
-------------------

LDAP authentication is possible within the editor. This can work in combination with the default Django Model authentication backend.

Required packages
***********************

#. Python LDAP::

    apt-get install python-ldap libldap2-dev libsasl2-dev

#. Django LDAP::

    pip install django-auth-ldap

#. GnuTLS (for secure LDAP lookups only)::

    apt-get install libgnutls26

Configuration
*******************

#. Copy :file:`numbas/ldap_auth.py.dist` to :file:`numbas/ldap_auth.py` and edit, following the comments in that file.
#. In :file:`numbas/settings.py` uncomment the LDAP auth line in ``AUTHENTICATION_BACKENDS`` and the ``ldap_auth`` import line.

Shibboleth authentication
-------------------------

The editor also supports Shibboleth authentication, using the Django Remote User backend and the `django-shibboleth-remoteuser <https://github.com/Brown-University-Library/django-shibboleth-remoteuser>`_ middleware.

Configuration
*************

Apache setup for a Shibboleth service provider (SP) is beyond the scope of this installation guide, and depends on the setup of the local Identity Provider (IdP).

Once the SP is set up, do the following.

#. Copy :file:`shib_auth.py.dist` to :file:`shib_auth.py` and edit, following the comments in that file.
#. In :file:`settings.py` uncomment the relevant line in ``MIDDLEWARE_CLASSES``, the ``RemoteUser`` backend in ``AUTHENTICATION_BACKENDS``, and the ``shib_auth`` import line.

.. note::
    If any changes are made to the editor code, including editing the settings files, then for the web server to recognise these changes either ``touch`` the :file:`web/django.wsgi` file, or restart the Apache server.

