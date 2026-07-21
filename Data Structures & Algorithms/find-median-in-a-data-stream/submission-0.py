class MedianFinder:

    def __init__(self):
        self.small = []
        heapq.heapify(self.small)
        self.large = []
        heapq.heapify(self.large)
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.small) + 1 < len(self.large):
            mid = heapq.heappop(self.large)
            heapq.heappush(self.small, -mid)

    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-self.small[0] + self.large[0]) / 2 

        