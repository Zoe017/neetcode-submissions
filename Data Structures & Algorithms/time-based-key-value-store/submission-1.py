class TimeMap:

    def __init__(self):
        self.timeMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        pairs = self.timeMap[key]
        l = 0
        r = len(pairs) - 1
        res = float("-inf")
        if timestamp < pairs[0][0]:
            return ""
        while l <= r:
            m = (l + r) // 2
            if pairs[m][0] == timestamp:
                return pairs[m][1]
            elif pairs[m][0] < timestamp:
                res = max(res, m)
                l = m + 1
            else:
                r = m - 1
        return pairs[res][1]
