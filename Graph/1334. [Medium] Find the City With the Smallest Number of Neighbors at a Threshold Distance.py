# There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi,
# and given the integer distanceThreshold, return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold.
# If there are multiple such cities, return the city with the greatest number.
# Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.

import collections
import heapq

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Create an adjacency list where adj[a] contains all the neighbors of node a and the corresponding distance d it takes to move to the neighbor b
        adj = collections.defaultdict(list)
        for a, b, d in edges:
            adj[a].append((b, d))
            adj[b].append((a, d))

        # Store the neighbor number for each city
        result = {}
        
        # Perform the neighbor computation for each city
        for number in range(n):
            # Initialize a heap that stores the current_distance and the source_node
            heap = [(0, number)]

            # Needed to store the valid neighbors (including itself)
            neighborhood = set()
            
            # Perform Dijkstra's until the heap is empty
            while heap:
                distance, node = heapq.heappop(heap) # Pop and return the smallest item from the heap (heap[0]), maintaining the heap invariant
                if distance <= distanceThreshold and node not in neighborhood:
                    neighborhood.add(node)
                    for b, d in adj[node]:
                        heapq.heappush(heap, (distance + d, b))
            
            result[number] = len(neighborhood) - 1
        
        return max([k for k,v in result.items() if v == min(result.values())])

    
# Dynamic Programming - Graph - Shortest Path