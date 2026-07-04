class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for idx,t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                index = stack.pop()[1]
                res[index] += idx - index
            stack.append((t, idx))
        return res
