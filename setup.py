from setuptools import setup, find_packages

setup(
    name='django-category',
    version='0.1.1',
    description='Django categorize content app.',
    long_description = open('README.rst', 'r').read() + open('AUTHORS.rst', 'r').read() + open('CHANGELOG.rst', 'r').read(),
    author='Praekelt Foundation',
    author_email='dev@praekelt.com',
    license='BSD',
    url='http://github.com/praekelt/django-category',
    packages=find_packages(),
    include_package_data=True,
    test_suite="setuptest.SetupTestSuite",
    install_requires = [
        'Django',
        'south',
    ],
    tests_require=[
        'django-setuptest>=0.0.6',
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

