## What do this branch?

1. now possible use custom mixin
simple declare list of you mixins in settings:
```python
DOWNTIME_MIXIN = ['utils.utility.downtime_mixin', ]  # custom list of you mixins
DOWNTIME_NODATABASE_MODE = True  # Dont use DataBase for check maintance mode
```
where in you project present app named 'utils.utility' and function `downtime_mixin`

from real project:
```python
def downtime_mixin(self_object, request):
    result = request.user.is_superuser
    if not result:
        api_key = request.GET.get('api_key')
        setting_api_key = getattr(settings, 'DOWNTIME_ADTIONAL_API_KEY', None)
        result = api_key == setting_api_key
    return not result
```
I use Django Rest Framework, and stay possible to use API for maintenance works, so i just declare in settings.py DOWNTIME_ADTIONAL_API_KEY variable and use this for allow requests. Too i use check request super user. This can be possible only if append `downtime.middleware.DowntimeMiddleware` to end of the list MIDDLEWARE.
2. Also introduce new variable DOWNTIME_NODATABASE_MODE , in this case no database need, this is very important because do query to database every time - bad idea.

Summary my settings looks like:
```python
DOWNTIME = True
.
.
.
if DOWNTIME:
    DOWNTIME_EXEMPT_PATHS = (
        '/admin/',
        '/ru/accounts/login/',
        '/en/accounts/login/',
    )
    DOWNTIME_MIXIN = ['utils.utility.downtime_mixin', ]  # custom list of you mixins
    DOWNTIME_NODATABASE_MODE = True  # Dont use DataBase for check maintance mode
    INSTALLED_APPS = (*INSTALLED_APPS, 'downtime',)
    MIDDLEWARE += ['downtime.middleware.DowntimeMiddleware', ]
    # MIDDLEWARE.insert(0, 'downtime.middleware.DowntimeMiddleware', )

    # private params
    DOWNTIME_ADDITIONAL_API_KEY = 'super-puper-secret-key'
```


--------------------------------- END

## Django Downtime

> Looking For Authors!  This project is currently looking for a user to take it over.  If that sounds like you, send a note to derek at stegelman dot com or open up an issue in this repository.

Small, simple, app to show a down page while you make upgrades.

Official Docs
-------------

http://django-downtime.readthedocs.org

Install
-------

Django supports versions 1.8, 1.9, 1.10, and 1.11 on Python 2 and 3.

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
