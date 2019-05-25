djangoquickstart
================

To run locally:

#. Create a Python 3.6 virtualenv::

    virtualenv my-env

    source my-env/bin/activate

#. Clone the git repository::
    
    git clone https://github.com/ShafiurShamim/djangoquickstart.git

#. Install dependencies::

    pip install -r requirements/dev.txt

#. Create 'secrets.json' or rename the file 'secrets.example.json' to 'secrets.json', containing something like::

    {
        "project_name": "djangoquickstart",
        "secret_key": "your-secret-key",
        "project_settings": "djangoquickstart.settings.dev",
        "root_urlconf": "djangoquickstart.urls",
        "wsgi_application": "djangoquickstart.wsgi.application",
        "debug": true,
        "allowed_hosts": []
    }

#. Run the test suit::

    python manage.py test

#. Finally run the server::

    python manage.py runserver