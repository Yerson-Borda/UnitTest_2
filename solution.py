from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        # This is not part of the initial code, just to handle not allowed input *- Bug -*
        if not (1 <= len(heights) <= 10 ** 5):
            raise ValueError("Error")
        if not all(0 <= h <= 10 ** 4 for h in heights):
            raise ValueError("Error")
        # This is not part of the initial code, just to handle not allowed input *- Bug -*

        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea


if __name__ == '__main__':
    result = Solution().largestRectangleArea([8, 18])
    print(result)
