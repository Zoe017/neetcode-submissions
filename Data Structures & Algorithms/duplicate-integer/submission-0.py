class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            new_list = nums[:i] + nums[i+1:]
            for n in new_list:
                if nums[i] == n:
                    return True
        return False

                
        