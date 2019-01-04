Django Category
===============
**Simple category app providing category and tag models.**

.. image:: https://travis-ci.org/praekelt/django-category.svg
    :target: https://travis-ci.org/praekelt/django-category
    :alt: Travis

.. image:: https://coveralls.io/repos/github/praekelt/django-category/badge.svg?branch=develop
    :target: https://coveralls.io/github/praekelt/django-category?branch=develop
    :alt: Coveralls

.. image:: https://badge.fury.io/py/django-category.svg
    :target: https://badge.fury.io/py/django-category
    :alt: Release

.. contents:: Contents
    :depth: 5

Requirements
------------

#. Python 2.7, 3.5-3.7

#. Django 1.11, 2.0, 2.1


Installation
------------

#. Install or add ``django-category`` to your Python path.

#. Add ``category`` to your ``INSTALLED_APPS`` setting.

#. This package uses django's internal sites framework. Add  ``django.contrib.sites`` to your ``INSTALLED_APPS``
   setting and include the required ``SITE_ID = 1`` (or similiar). The official docs can be found here:
   https://docs.djangoproject.com/en/2.1/ref/contrib/sites/.

#. Optional: ``django-object-tools`` provides a category tree view. See https://github.com/praekelt/django-object-tools
   for installation instructions.

Usage
-----

Enable categorization and/or tagging on a model by creating ``ManyToMany`` fields to the models provided by ``django-category``, for example::

    from django import models

    class MyModel(models.Model):
        categories = models.ManyToManyField(
            'category.Category',
            help_text='Categorize this item.'
        )
        tags = models.ManyToManyField(
            'category.Tag',
            help_text='Tag this item.'
        )

Models
------

class Category
~~~~~~~~~~~~~~
Category model to be used for categorization of content. Categories are high level constructs to be used for grouping and organizing content, thus creating a site's table of contents.

Category.title
++++++++++++++
Short descriptive title for the category to be used for display.


Category.subtitle
+++++++++++++++++
Some titles may be the same and cause confusion in admin UI. A subtitle makes a distinction.

Category.slug
+++++++++++++
Short descriptive unique name to be used in urls.

Category.parent
+++++++++++++++
Optional parent to allow nesting of categories.

Category.sites
++++++++++++++
Limits category scope to selected sites.

class Tag
~~~~~~~~~
Tag model to be used for tagging content. Tags are to be used to describe your content in more detail, in essence providing keywords associated with your content. Tags can also be seen as micro-categorization of a site's content.

Tag.title
+++++++++
Short descriptive name for the tag to be used for display.

Tag.slug
++++++++
Short descriptive unique name to be used in urls.

Tag.categories
++++++++++++++
Categories to which the tag belongs.

