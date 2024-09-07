
from collections import deque, defaultdict

class Solution:
    def shortestPath(self, edges, n, m, src):
        print(edges)
        # Step 1: Create adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        print("adj:",adj)
        
        # Step 2: Initialize distances array
        dist = [-1] * n
        dist[src] = 0
        print("dist:",dist)
        
        # Step 3: Perform BFS
        queue = deque([src])
        
        while queue:
            node = queue.popleft()
            print("node:",node)
            
            for neighbor in adj[node]:
                print("Neighbor:",neighbor)
                if dist[neighbor] == -1:  # If not visited
                    print("dist:",dist)
                    dist[neighbor] = dist[node] + 1
                    print("dist[neighbor] = dist[node] + 1 -->",dist[neighbor] ,"=", dist[node] ,'+', 1)
                    print("dist:",dist)
                    queue.append(neighbor)
                    print("Q:",queue)
                print()
            print()
        
        return dist

n = 9
m = 10
edges=[[0,1],[0,3],[3,4],[4,5],[5,6],[1,2],[2,6],[6,7],[7,8],[6,8]] 
src=0
obj=Solution()
print(obj.shortestPath(edges, n, m, src))