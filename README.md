## Django Downtime

Small, simple, app to show a down page while you make upgrades.

Official Docs
-------------

http://django-downtime.readthedocs.org

Install
-------

Django supports versions 1.8 and 1.9 on Python 2 and 3.

To install django-downtime::

    pip install django-downtime

add to installed apps::

    downtime

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

Url Redirect

    DOWNTIME_URL_REDIRECT = "http://errors.mypage.com"

Templates
---------

If no URL Redirect is specified a ``lame`` default template is rendered, this can be overridden
by specifying a ``downtime/downtime.html`` template.

Management Commands
-------------------

There are two managment commands, one to take a project down `python manage.py downtime_start` and one to set it back
up `python manage.py downtime_end`.

What happens internally when calling `python manage.py downtime_start`?

This sets a start date time and mark is as enabled. We call this "deployment mode", usually called before
running a deployment script.

What happens internally when calling `python manage.py downtime_end`?

This sets a end date time to all records that has a start date time and no end date time set and are
marked as enabled. We call this "closing deployment mode", usually called after running a deployment script.
