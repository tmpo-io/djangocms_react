#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

    environment = os.getenv('ENV')
    if not environment:
        try:
            with open(
                os.path.join(os.path.dirname(__file__), '..', 'environment'), 'r'
            ) as _file:
                environment = _file.read().replace('\n', '')
        except IOError:
            print '\033[91m!!!!!ERROR!!!!'
            print ('\033[1;38mProvide an environment file in the repo root src/environment')
            print "----"
            print "echo 'dev' > ../environment"
            print "\033[1;m"
            sys.exit(1)

    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "{{ cookiecutter.project_name }}.settings.%s" % environment
    )

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
