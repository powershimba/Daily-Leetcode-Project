"""
1480. Running Sum of 1d Array

Given an array nums. 
We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.
"""


class Solution(object):
    def runningSum(self, nums):
        output = []
        for i in range(len(nums)):
            sum = 0
            for j in range(i+1):
                sum += nums[j]
            output.append(sum)
        return output

"""
More Simple Solution
=> Using fibonacci sequence

class Solution(object):
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums
"""