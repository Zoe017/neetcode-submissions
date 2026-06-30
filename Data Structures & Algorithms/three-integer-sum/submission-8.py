class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        stay = 0;
        result = []
        while stay < len(nums) - 2 and nums[stay] <= 0:
            if stay > 0 and nums[stay] == nums[stay - 1]:
                stay += 1
                continue
            s = 0 - nums[stay]
            left = stay + 1
            right = len(nums) - 1
            while left < right:
                if (nums[left] + nums[right] > s):
                    right = right - 1
                elif nums[left] + nums[right] < s:
                    left = left + 1
                else:
                    result.append([nums[stay], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
            stay = stay + 1
        return result
