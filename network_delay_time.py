from collections import defaultdict
import heapq
'''
This problem is solved using Dijkstra's algorithm.(BFS: Breadth first search)
Concepts used: 
1. adjecency matrix to store the edges and weights
2. heapq to update the shortest path from the starting node
3. set of visited nodes so that all the nodes are traversed exactly once.
'''

from collections import defaultdict
import heapq
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        # cretae a hashMap of edges
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        # create a min heap (priority queue)
        minHeap = [(0, k)]
        visited = set()
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            t = max(t, w1)
            for n2, w2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return t if len(visited) == n else -1

