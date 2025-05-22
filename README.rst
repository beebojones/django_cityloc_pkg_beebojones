===============
City Locations
===============

City Locations is a Django app that can be installed in an existing Django project.

Installation
------------

1. Add "citylocations" to your INSTALLED_APPS setting in settings.py:

    INSTALLED_APPS = [
        ...
        'citylocations',
    ]

2. Include the citylocations URLconf in your project urls.py:

    path('', include('citylocations.urls')),

3. Run server and visit http://127.0.0.1:8000/
