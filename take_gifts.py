'''
Problem: 2558 Leetcode Easy
Link: https://leetcode.com/problems/take-gifts-from-the-richest-pile/
Approach: Heap(max heap)
1. create a maxheap
2. for i in range(k):
    max := heap.pop()
    heap.push(floor(sqrt(max)))
3. return sum(heap)
'''

import heapq
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
    #    create a max heap
        maxheap = [-1 * g for g in gifts]
        heapq.heapify(maxheap)
        for i in range(k):
            maximum = heapq.heappop(maxheap)
            maximum = -1 * int(math.sqrt(abs(maximum)))
            heapq.heappush(maxheap, maximum)
            # print(maxheap)
        return(sum([abs(e) for e in maxheap]))
