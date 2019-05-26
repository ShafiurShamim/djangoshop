djangoshop
==========

To run locally:

#. Create a Python 3.6 virtualenv::

    virtualenv djangoshop

    source djangoshop/bin/activate

#. Clone the git repository::
    
    git clone https://github.com/ShafiurShamim/djangoshop.git
    
    cd djangoshop

#. Install dependencies::

    pip install -r requirements/dev.txt

#. Create 'secrets.json' or rename the file 'secrets.example.json' to 'secrets.json', containing something like::

    {
        "project_name": "djangoshop",
        "secret_key": "your-secret-key",
        "project_settings": "djangoshop.settings.dev",
        "root_urlconf": "djangoshop.urls",
        "wsgi_application": "djangoshop.wsgi.application",
        "debug": true,
        "allowed_hosts": []
    }

#. Run the test suit::

    python manage.py test

#. Finally run the server::

    python manage.py runserver