# Brute Force
class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        sum = 0
        for i in range(len(nums)-1):
            if i==0 or i%2 == 0:
                sum += nums[i]
        # sum(nums[i] for i in range(0, len(nums), 2))
        return sum
        """
        :type nums: List[int]
        :rtype: int
        """
        