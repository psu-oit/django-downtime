=====
Usage
=====

Adding Downtime
---------------

Using the admin site
~~~~~~~~~~~~~~~~~~~~

Head on over to the django admin and add a new ``period`` instance.  It is recommended to add your admin site
to the tuple of ``DOWNTIME_EXEMPT_PATHS`` so that you can still login and bring the site online earlier than scheduled.

Using the management command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use `python manage.py downtime_start` to start an unscheduled downtime. This sets a start date time and mark is as enabled.
We call this "deployment mode", usually called before running a deployment script.

Bringing The Site Back Up
-------------------------

Using the admin site
~~~~~~~~~~~~~~~~~~~~

Either delete the ``Period`` instance or uncheck ``enable`` for the current downtime instance.

Using the management command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To set the site back up run `python manage.py downtime_end`.

This sets a end date time to all records that has a start date time and no end date time set and are
marked as enabled. We call this "closing deployment mode", usually called after running a deployment script.
