class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        tCount = {}
        sCount = {}
        minlen = float('inf')
        res = ""
        match = 0

        for i in range(len(t)):
            tCount[t[i]] = tCount.get(t[i], 0) +1

        need = len(tCount.keys())
        l = 0
        for r in range(len(s)):
            curr = s[r]
            if curr in tCount:
                sCount[curr] = sCount.get(curr,0) + 1
                if sCount[curr] == tCount[curr]:
                    match += 1
            while match == need:
                if r - l + 1 < minlen:
                    res = s[l:r + 1]
                    minlen = r - l + 1
                left = s[l]
                if left in tCount:
                    sCount[left] -= 1
                    if tCount[left] > sCount[left]:
                        match -= 1
                l += 1
        return res

