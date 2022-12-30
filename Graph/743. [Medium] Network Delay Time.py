# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi),
# where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal.
# If it is impossible for all the n nodes to receive the signal, return -1.

import collections
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Create an adjacency list where adj[a] contains all the neighbors of node a and the corresponding time t it takes to move to the neighbor b
        adj = collections.defaultdict(list)
        for a, b, t in times:
            adj[a].append((b,t))     
        
        # Initialize a heap that stores the current_time and the source_node
        heap = [(0, k)]

        # Needed to store the arrival time for each reachable node
        node_time = {}
        
        # Perform Dijkstra's until the heap is empty
        while heap:
            time, node = heapq.heappop(heap) # Pop and return the smallest item from the heap (heap[0]), maintaining the heap invariant
            if node not in node_time:
                node_time[node] = time

                for b, t in adj[node]:
                    heapq.heappush(heap, (time + t, b))

        return max(node_time.values()) if len(node_time) == n else -1   # With check if all nodes are reachable


# Depth-First Search - Breadth-First Search - Graph - Heap (Priority Queue) - Shortest Path
