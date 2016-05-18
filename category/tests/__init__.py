import unittest

from category import admin, models


class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cat1 = models.Category.objects.create(title="Cat 1", slug="cat1")
        cls.cat2 = models.Category.objects.create(title="Cat 2", slug="cat2")

    def test_circular_reference(self):
        """Confirm a category cannot have itself as an ancestor"""
        self.cat1.parent = self.cat2
        self.cat1.save()
        self.cat2.parent = self.cat1
        self.assertRaises(RuntimeError, self.cat2.save)
