import sys
from StringIO import StringIO

from coverage import coverage
from django.conf import settings
import pep8

MODULE = 'category'

if not settings.configured:
    settings.configure(
        DATABASE_ENGINE='sqlite3',
        INSTALLED_APPS=[
            'category',
        ],
    )

from django.test.simple import run_tests

def runpep8():
    # Hook into stdout.
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    # Run Pep8 checks.
    pep8.options, pep8.args = pep8.process_options()
    pep8.input_dir(MODULE)

    # Restore stdout.
    sys.stdout = old_stdout

    # Save result to pep8.txt.
    result = mystdout.getvalue()
    output = open('pep8.txt', 'w')
    output.write(result)
    output.close()

    # Return Pep8 result
    return result

def runtests():
    # Start coverage.
    cov = coverage()
    cov.start()

    # Run tests.
    failures = run_tests((MODULE,), verbosity=1, interactive=True)
   
    # Stop and generate coverage report.
    cov.stop()
    print "\nCoverage Report:"
    cov.report(include=['%s*' % MODULE,])
    cov.xml_report(include=['%s*' % MODULE,])

    print "\nPEP8 Result:"
    print runpep8()

    sys.exit(failures)

if __name__ == '__main__':
    runtests()
