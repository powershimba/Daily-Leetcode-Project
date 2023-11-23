"""
46. Permutations
Medium
"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtracking(curr):
            if len(curr) == len(nums):
                output.append(curr[:])
                return
            
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtracking(curr)
                    curr.pop()
                
        output = []
        backtracking([])
        return output
                
        

