#!/usr/bin/env python
import os
import sys
import warnings

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bongo.settings.dev")

    from django.core.management import execute_from_command_line


    with warnings.catch_warnings():
        warnings.filterwarnings("ignore",category=DeprecationWarning)
        import django.contrib.contenttypes.generic

    execute_from_command_line(sys.argv)
