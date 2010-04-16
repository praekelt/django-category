from django.db import models

class Category(models.Model):
    title = models.CharField(
        max_length=64,
        help_text='Short descriptive name for this category.',
    )

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
