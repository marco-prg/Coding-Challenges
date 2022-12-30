# There are n cities connected by some number of flights.
# You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.
# You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

import collections
import heapq

class Solution:
    # TIME LIMIT EXCEEDED
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Create an adjacency list where f[a] contains all the neighbors of node a and the corresponding price p it takes to move to the neighbor b
        f = collections.defaultdict(dict)
        for a, b, p in flights:
            f[a][b] = p
        
        # Initialize a heap that stores a triplet: current_price, current_city, remaining_steps
        heap = [(0, src, k + 1)]
        
        # Perform Dijkstra's until the heap is empty
        while heap:
            p, i, k = heapq.heappop(heap) # Pop and return the smallest item from the heap (heap[0]), maintaining the heap invariant
            if i == dst:
                return p
            if k > 0:
                for j in f[i]:
                    heapq.heappush(heap, (p + f[i][j], j, k - 1))
        # Cannot reach the destination
        return -1


# Dynamic Programming - Depth-First Search - Breadth-First Search - Graph - Heap (Priority Queue) - Shortest Path