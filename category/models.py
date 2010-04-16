from django.db import models

class Category(models.Model):
    title = models.CharField(
        max_length=64,
        help_text='Short descriptive name for this category.',
    )
