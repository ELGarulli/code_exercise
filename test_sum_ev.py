import unittest
from main import sum_ev


class TestComputeEvenChanges(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(sum_ev([1, 2, 3, 4]), 6)
    # add here additional tests