# 207. Course Schedule
# Medium

# Problem: Figure out whether cycle is or not in directed graph

# 1. Topological Sort
#   1) Start from vertex with 0 in-degree
#   2) Delete edges from current vertex
#   3) Move to adjecent vertex which has 0 in-degree
#   4) When process is done, 
#       return True(no cycle, possible to complete) if the num(visited vertex) == num(all courses), 
#       otherwise return False
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Save the number of indegree edges of each vertex
        #   indegree: List[int] / index: node position / value: the number of indegree edges
        indegree = [0] * numCourses

        # Save adjacent vertexes of each vertex
        #   adj: List[List[int]] / index: node position / value(List[int]): list of adjacent vertexes
        adj = [ [] for _ in range(numCourses)]

        for pre in prerequisites:
            adj[pre[1]].append(pre[0])
            indegree[pre[0]] += 1
        
        # queue for adjacent vertex of current vertex
        queue = deque()

        # check visited vertex
        visited = 0

        # Insert vertex with 0 indegree
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i) 
        
        # Iterate queue 
        #   deleting out degree edge from current vertex
        #   while vertex with 0 indegree doesn't left
        while queue:
            node = queue.popleft()
            visited += 1
            for i in adj[node]: # i: int
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        
        return visited == numCourses
   
# 2. DFS
#   1) Iterate all vertex, tracking adjacent vertexes of each node recursively
#   2) while tracking vertexes, find same vertex during ongoing track, turn True(dectect cycle)
#   3) if one of the step in dfs stack  

class Solution(object):
    # We need 1) curr index 2) adj list of curr ptr 3) tracked storage 4) visited node
    def dfs(self, curr, adj, track, visited):
        if track[curr]:
            return True
        if visited[curr]:
            return False
        
        track[curr] = True
        visited[curr] = True

        for node in adj[curr]:
            if self.dfs(node, adj, track, visited):
                return True
        
        track[curr] = False
        return False

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj = [[] for _ in range(numCourses)]
        for pre in prerequisites:
            adj[pre[1]].append(pre[0])
        visited = [False] * numCourses
        track = [False] * numCourses
        for i in range(numCourses):
            if self.dfs(i, adj, track, visited):
                return False
        return True 
