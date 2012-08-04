=====
Usage
=====

Adding Downtime
---------------

Head on over to the django admin and add a new ``period`` instance.  It is recommended to add your admin site
to the tuple of ``DOWNTIME_EXEMPT_PATHS`` so that you can still login and bring the site online earlier.

Bringing The Site Back Up
-------------------------

Either delete the ``Period`` instance or uncheck ``enable`` for the current downtime instance.