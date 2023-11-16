# 200. Number of Islands
# Graph, dfs

# Noticethe type of element: It's String, not Integer!
class Solution(object):
    
    def numIslands(self, grid):
        def isLand(i, j):
            # if grid[i, j] is not land, quit function
            if i < 0 or i >= len(grid) or \
                j < 0 or j >= len(grid[0]) or \
                grid[i][j] != '1':
                    return
            # otherwise, change grid[i, j] => 0
            grid[i][j] = 0
            
            # Probe adjacent elements recursively
            isLand(i+1, j)
            isLand(i-1, j)
            isLand(i, j+1)
            isLand(i, j-1)
        
        # travel grid with isLand function
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    isLand(i, j)
                    cnt += 1
        return cnt        

        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
