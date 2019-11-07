from django.test import TestCase


class Test(TestCase):
    def setUp(self):
        self.value = 6

    def test(self):
        self.assertEqual(self.value, 6)
