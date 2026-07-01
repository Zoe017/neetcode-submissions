class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        buy = float('inf')
        for p in prices:
            if p < buy:
                buy = p
            elif p - buy > m:
                m = p - buy
        return m