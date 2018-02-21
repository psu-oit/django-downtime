#!/usr/bin/env python

import os, sys
from django.conf import settings
import django

DIRNAME = os.path.dirname(__file__)

settings.configure(
    DEBUG=True,
    DATABASES={
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           }
    },
    INSTALLED_APPS=('django.contrib.auth',
                   'django.contrib.contenttypes',
                   'django.contrib.sessions',
                   'django.contrib.admin',
                   'downtime',),
    TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.contrib.auth.context_processors.auth',
                ],
            },
        },
    ],
    USE_TZ=True,
    TIME_ZONE="UTC"
)


django.setup()

from django.test.runner import DiscoverRunner
test_runner = DiscoverRunner(verbosity=1)

failures = test_runner.run_tests(['downtime', ])
if failures:
    sys.exit(failures)
