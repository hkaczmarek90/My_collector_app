import unittest
from counter import MySolution as ms

test_object = ms(3, 6, 9, 3)


class MyTestCase(unittest.TestCase):
    def test_small_box(self):
        self.assertEqual(test_object.without_collect_box(2), 'Only 1 small box', 'Should be Only 1 small box')

    def test_medium_box(self):
        self.assertEqual(test_object.without_collect_box(4), 'Only 1 medium box', 'Should be Only 1 medium box')

    def test_large_box(self):
        self.assertEqual(test_object.without_collect_box(8), 'Only 1 large box', 'Should be Only 1 large box')

    def test_collect_box(self):
        self.assertIsNotNone(test_object.check_box(10))

    def test_count1(self):
        self.assertEqual(test_object.count(3), test_object.without_collect_box(3))

    def test_count2(self):
        self.assertIs(test_object.count(10), test_object.count(11))


if __name__ == '__main__':
    unittest.main()
