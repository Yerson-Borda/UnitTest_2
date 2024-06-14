<div align="center">
  <h1>Largest Rectangle in Histogram - Unit Testing</h1>
</div>

This project contains the implementation and unit tests for finding the area of the largest rectangle in a histogram given an array of integers representing the heights of the histogram's bars.

## Solution

The `Solution` class implements the method `largestRectangleArea` which takes a list of integers `heights` and returns the area of the largest rectangle in the histogram.
The test suite for the Solution class is implemented using the unittest library. It includes various tests to ensure the correctness and robustness of the largestRectangleArea method by test cases of basic functionality and edge cases.

### Constraints
- `1 <= heights.length <= 100000`
- `0 <= heights[i] <= 10000`

## Finding and Reporting Bugs

During testing, if the constraints are not handled correctly, the method will raise a ValueError. The tests test_exceeding_number_of_bars and test_exceeding_height ensure that invalid inputs are correctly identified and handled by raising appropriate exceptions.

### Fixing Detected Bugs
The detected bug was the lack of constraint checks in the largestRectangleArea method. The method has been updated to include the following constraint checks:
```python
if not (1 <= len(heights) <= 10 ** 5):
    raise ValueError("The length of heights must be between 1 and 100,000.")
if not all(0 <= h <= 10 ** 4 for h in heights):
    raise ValueError("All heights must be between 0 and 10,000.")
```
This ensures that invalid inputs are correctly handled and reported.
