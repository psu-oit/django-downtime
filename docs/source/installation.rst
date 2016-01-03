============
Installation
============

Django Downtime supports Django 1.8 - 1.9 and Python 2 and 3.


To install django-downtime::

    pip install django-downtime

add to installed apps::

    INSTALLED_APPS += (
        'downtime',
    )

Add downtime middleware to ``the top`` your list of installed middlewares::

    'downtime.middleware.DowntimeMiddleware',


Settings
--------

Exempted URLs::

    DOWNTIME_EXEMPT_EXACT_URLS = (
        '/', # exempts homepage
        '/other_location/not_down/page',
    )

Exempted Paths::

    DOWNTIME_EXEMPT_PATHS = (
        '/admin',
        '/other_location_not_down',
    )

Url Redirect::

    DOWNTIME_URL_REDIRECT = "http://errors.mypage.com"

Templates
---------

If no URL Redirect is specified a ``lame`` default template is rendered, this can be overridden
by specifying a ``downtime/downtime.html`` template.
