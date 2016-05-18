Django Category
===============
**Simple category app providing category and tag models.**

.. figure:: https://travis-ci.org/praekelt/django-category.svg?branch=develop
   :align: center
   :alt: Travis

.. contents:: Contents
    :depth: 5

Installation
------------

#. Install or add ``django-category`` to your Python path.

#. Add ``category`` to your ``INSTALLED_APPS`` setting.

#. If you are on Django < 1.7 then add ``south`` to your ``INSTALLED_APPS`` setting.

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

