from setuptools import setup, find_packages
from setuptools.command.test import test

def run_tests(self):
    from setuptest.runtests import runtests
    return runtests(self)
test.run_tests = run_tests

setup(
    name='django-category',
    version='0.0.4',
    description='Django categorize content app.',
    long_description = open('README.rst', 'r').read() + open('AUTHORS.rst', 'r').read() + open('CHANGELOG.rst', 'r').read(),
    author='Praekelt Foundation',
    author_email='dev@praekelt.com',
    license='BSD',
    url='http://github.com/praekelt/django-category',
    packages=find_packages(),
    include_package_data=True,
    test_suite="category.tests",
    tests_require=[
        'django-setuptest',
    ],
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)

