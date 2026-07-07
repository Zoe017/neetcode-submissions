class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                idx, height = stack.pop()
                area = max(area, height*(i-idx))
                start = idx
            stack.append([start,heights[i]])

        for j, h in stack:
            area = max(area, h * (len(heights) - j))
        return area
