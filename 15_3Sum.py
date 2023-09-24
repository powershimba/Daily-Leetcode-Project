# Use center pointer
# Time Complexity: O(n2), 6635ms(5.02%)
# Memory Complexity: 17.22MB(15.65%)
class Solution(object):
    def threeSum(self, nums):
        result = []
        nums.sort()

        for c in range(1, len(nums)-1):
            l = c-1
            r = c+1

            while True:
                sum = nums[c] + nums[l] + nums[r]
                if sum == 0:
                    if [nums[c], nums[l], nums[r]] not in result:
                        result.append([nums[c], nums[l], nums[r]])
                    if r<len(nums)-1 and l>0:
                        r += 1
                        l -= 1
                    else: break
                elif sum < 0 and r<len(nums)-1:
                    r += 1
                elif sum > 0 and l>0:
                    l -= 1
                else:
                    break
        return result        
                    
# Brute Force
# Time Complexity: O(n3), Time Limit Exceeded(308/312 testcases passed)
class Solution(object):
    def threeSum(self, nums):
        result = []
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        sorted_nums = sorted([nums[i], nums[j], nums[k]])
                        if sorted_nums not in result:
                            result.append(sorted_nums)
        return result

        #type nums: List[int]
        #rtype: List[List[int]]