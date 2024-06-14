import unittest
from solution import Solution


class TestLargestRectangleArea(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_heights(self):
        """Test with an empty histogram."""
        # self.assertEqual(self.solution.largestRectangleArea([]), 0)
        with self.assertRaises(ValueError):
            self.solution.largestRectangleArea([])

    def test_single_bar(self):
        """Test with a histogram containing a single bar."""
        self.assertEqual(self.solution.largestRectangleArea([5]), 5)

    def test_two_bars(self):
        """Test with a histogram containing two bars."""
        self.assertEqual(self.solution.largestRectangleArea([2, 4]), 4)

    def test_increasing_heights(self):
        """Test with a histogram where bar heights are strictly increasing."""
        self.assertEqual(self.solution.largestRectangleArea([1, 2, 3, 4, 5]), 9)

    def test_decreasing_heights(self):
        """Test with a histogram where bar heights are strictly decreasing."""
        self.assertEqual(self.solution.largestRectangleArea([5, 4, 3, 2, 1]), 9)

    def test_random_heights(self):
        """Test with a histogram of random heights."""
        self.assertEqual(self.solution.largestRectangleArea([2, 1, 5, 6, 2, 3]), 10)

    def test_all_same_height(self):
        """Test with a histogram where all bars are of the same height."""
        self.assertEqual(self.solution.largestRectangleArea([4, 4, 4, 4, 4]), 20)

    def test_zero_heights(self):
        """Test with a histogram containing bars of height zero."""
        self.assertEqual(self.solution.largestRectangleArea([0, 0, 0, 0, 0]), 0)

    def test_mixed_zero_nonzero_heights(self):
        """Test with a histogram containing mixed zero and non-zero heights."""
        self.assertEqual(self.solution.largestRectangleArea([0, 2, 0, 3, 0]), 3)

    def test_minimum_height_maximum_bars_input(self):
        """Test with the maximum number of bars and minimum heights."""
        max_heights = [1] * 100000
        self.assertEqual(self.solution.largestRectangleArea(max_heights), 100000)

    def test_max_height_maximum_bars_input(self):
        """Test with the maximum number of bars and maximum possible heights."""
        max_heights = [10000] * 100000
        self.assertEqual(self.solution.largestRectangleArea(max_heights), 10 ** 9)

    def test_exceeding_number_of_bars(self):
        """Test with more than the maximum number of bars."""
        exceeding_heights = [1] * 100001  # 100001 bars, exceeds the constraint
        with self.assertRaises(ValueError):
            self.solution.largestRectangleArea(exceeding_heights)

    def test_exceeding_height(self):
        """Test with a bar height exceeding the maximum height."""
        exceeding_heights = [10001] * 100000  # Heights exceed the constraint
        with self.assertRaises(ValueError):
            self.solution.largestRectangleArea(exceeding_heights)


if __name__ == '__main__':
    unittest.main()
