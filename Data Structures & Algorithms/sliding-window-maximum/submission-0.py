class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        l = 0
        for r in range(k, len(nums)+ 1):
            curr = nums[l : r]
            output.append(max(curr))
            l += 1
        return output