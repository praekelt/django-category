from setuptools import setup, find_packages

setup(
    name='django-category',
    version='dev',
    description='Django categorize app.',
    author='Praekelt Consulting',
    author_email='dev@praekelt.com',
    url='https://github.com/praekelt/django-category',
    packages = find_packages(),
    include_package_data=True,
)
