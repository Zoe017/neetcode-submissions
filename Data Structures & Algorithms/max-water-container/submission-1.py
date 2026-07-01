class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        for i in range(len(heights)):
            for j in range(i,len(heights)):
                width = j - i
                area = width * min(heights[i],heights[j])
                result = max(area, result)
        return result