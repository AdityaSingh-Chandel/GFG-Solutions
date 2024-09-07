from collections import defaultdict, deque
from typing import List

class Solution:
    def findOrder(self, dict: List[str], n: int, k: int) -> str:
        # Step 1: Create a graph (Adjacency list)
        graph = defaultdict(list)
        print(graph)
        indegree = [0] * k
        print("indegree:",indegree)
        
        # Step 2: Build the graph by comparing adjacent words
        for i in range(n - 1):
            word1 = dict[i]
            word2 = dict[i + 1]
            min_len = min(len(word1), len(word2))
            for j in range(min_len):
                if word1[j] != word2[j]:
                    # There is a precedence word1[j] -> word2[j]
                    # Convert character to index (0-based index)
                    u = ord(word1[j]) - ord('a')
                    v = ord(word2[j]) - ord('a')
                    
                    # Only add the edge if it's not already present to avoid duplicates
                    if v not in graph[u]:
                        graph[u].append(v)
                        indegree[v] += 1
                    break
        print("indeg:",indegree)
        # Step 3: Perform topological sort using Kahn's Algorithm (BFS)
        queue = deque()
        # Add all characters with 0 indegree (i.e., no dependencies)
        for i in range(k):
            if indegree[i] == 0:
                queue.append(i)
        
        topo_order = []
        while queue:
            node = queue.popleft()
            topo_order.append(chr(node + ord('a')))
            
            # Decrease the indegree of the neighbors
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If topo_order contains all characters, it's a valid order
        if len(topo_order) == k:
            return "".join(topo_order)
        else:
            return ""  # In case of a cycle or invalid input


n = 5
k = 4
dict = ["baa","abcd","abca","cab","cad"]
obj=Solution()
print(obj.findOrder(dict,n,k))
