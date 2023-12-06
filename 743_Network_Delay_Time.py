# Djikstra's Solution using heap DS
ass Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        # Dijkstra's solution

        # graph = {start: [(dest, dist), (), ...]}
        graph = defaultdict(list)
        for src, dst, dist in times:
          graph[src].append((dst, dist)) 

        queue = [(0, k)] # (cost, node)
        visited = set()
        max_cost = 0

        while queue:
          cost, node = heapq.heappop(queue)

          if node in visited:
            continue

          visited.add(node)
          max_cost = max(max_cost, cost)

          neighbours = graph[node]
          for neighbour in neighbours:
            new_node, new_cost = neighbour
          
            if new_node not in visited:
              curr_cost = new_cost + cost
              heapq.heappush(queue, (curr_cost, new_node))

        return max_cost if len(visited) == n else -1

