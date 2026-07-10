class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        minH = float("inf")
        minK = r
        while l <= r:
            k = (r + l) // 2
            hour = 0
            for p in piles:
                hour += math.ceil(p/k)
                if hour > h:
                    l = k + 1
                    break
            if hour <= h:
                minK = min(minK, k)
                r = k - 1
        return minK

        
        