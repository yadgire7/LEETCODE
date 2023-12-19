'''
Approach: Max Heap
'''

import heapq
import copy

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        cost = 0
        for i in range(len(grid[0])):
            iter_cost = -1
            for row in grid:
                max_heap_row = [-1 * ele for ele in row]
                heapq.heapify(max_heap_row)
                largest = heapq.heappop(max_heap_row)
                if iter_cost < (-1 * largest):
                    iter_cost = -1 * largest
                row.pop(row.index(-1 * largest))
            cost += iter_cost
        return cost
            
        