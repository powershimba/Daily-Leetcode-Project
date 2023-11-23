"""
39. Combination Sum
Medium
Graph, dfs, recursive, backtracking
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(curr, start):
            if sum(curr) > target:
                return
            if sum(curr) == target:
                ans.append(curr[:])
                return
            for num in range(start, len(candidates)):
                curr.append(candidates[num])
                dfs(curr, num)
                curr.pop()
        
        ans = []
        dfs([], 0)
        return ans
