class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = [-x for x in stones]
        heapq.heapify(minHeap) 
        while len(minHeap) > 1:
            a = heapq.heappop(minHeap)
            b = heapq.heappop(minHeap)
            if a == b:
                continue
            else:
                heapq.heappush(minHeap, a - b)
        return -minHeap[0] if minHeap else 0

