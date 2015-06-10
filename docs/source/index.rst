.. Django Downtime documentation master file, created by
   sphinx-quickstart on Sat Aug  4 14:37:46 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Django Downtime!
===========================


Overview
--------

Small, simple, app to show a down page while you make upgrades.

Purpose
-------

This app simply runs middleware that checks to see if the site is down for maintenance.
If it is, (with a period of downtime added to the apps models) either a redirect occurs or a
template is loaded with a down time message.  This app isn't intended to be a full service solution
as it still requires that the django site remain functional to work.  In other cases it may be more
beneficial to point your domain at a different server instead.


Contents:

.. toctree::
   :maxdepth: 2

   installation
   usage
   contributors
   changelog
   license

