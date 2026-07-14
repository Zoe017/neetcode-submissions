class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        find = nums[0]
        while True:
            if find == slow:
                return find
            find = nums[find]
            slow = nums[slow]
        return