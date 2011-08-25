import sys

from coverage import coverage
from django.conf import settings

if not settings.configured:
    settings.configure(
        DATABASE_ENGINE='sqlite3',
        INSTALLED_APPS=[
            'category',
        ],
    )

from django.test.simple import run_tests

def runtests():
    # Start coverage.
    cov = coverage()
    cov.start()

    # Run tests.
    failures = run_tests(('category',), verbosity=1, interactive=True)
   
    # Stop and generate coverage report.
    cov.stop()
    cov.report(include=["category*",])
    cov.xml_report(include=["category*",])

    sys.exit(failures)

if __name__ == '__main__':
    runtests()
