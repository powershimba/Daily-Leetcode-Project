"""
78. Subsets
Medium
"""

# Cascading: add new element to the current elements
class Solution(object):
    def subsets(self, nums):
        output = [[]]
        for num in nums:
            output += [curr + [num] for curr in output]
        return output

# Backtracking: nested dfs function
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(curr, start, l):
            if len(curr) == l:
                ans.append(curr[:])
                return

            for num in range(start, len(nums)):
                curr.append(nums[num])
                dfs(curr, num+1, l)
                curr.pop()
                
        ans = [[]]
        for l in range(1, len(nums)):
            dfs([], 0, l)
        ans.append(nums)
        return ans
