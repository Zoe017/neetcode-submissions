class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        length = 0
        fre = {}
        for right in range(len(s)):
            fre[s[right]] = 1 + fre.get(s[right], 0)
            max_frequent = max(fre.values())
            while right - left + 1 - max_frequent > k:
                fre[s[left]] -= 1
                left += 1
            length = max(length, right - left + 1)
        return length