django-downtime
===============

Small, simple, app to show a down page while you make upgrades.  

Install
-------

To install django-downtime::

	pip install django-downtime
	
add to installed apps::

	downtime

Add downtime middleware to ``the top`` your list of installed middlewares::

    'downtime.middleware.DowntimeMiddleware',


Settings
--------

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
by specificing a ``downtime/downtime.html`` template.