# In this problem, a tree is an undirected graph that is connected and has no cycles.
# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added.
# The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.
# The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.
# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        def dfs(u,v):
			# if a node is visited we cannot find a path through it as it itself formed a cycle which we do not want
            if u in visited:
                return False
			# if dfs finally reached to the node 'v' means it has found path from 'u' to 'v'.
            if u == v:
                return True
            
			# mark the node of dfs as visited.
            visited.add(u)
            
			# each node connected to u, split the different dfs recursion path
            for i in graph[u]:
                if dfs(i, v):
                    return True
            return False       
        
        n = len(edges)      # Number of nodes
        graph = defaultdict(set) 
        
        ans = []
		# for each edge in edges
        for u, v in edges:
            visited = set()
			# perform dfs every time you add an edge
			# so that we if a cycle is formed we know exactly this edge has caused the cycle
            if dfs(u, v):
				# do not return the edge directly here
				# as we want the last possible edge that caused the cycle
                ans = [u,v]
			# add the edge and reverse edge in graph as it is undirected
            graph[u].add(v)
            graph[v].add(u)
        return ans


# Depth-First Search - Breadth-First Search - Union Find - Graph
