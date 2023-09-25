
"""
:type nums: List[int]
:rtype: List[int]
"""
        

# Create only one list that multiplies elements from the front of list nums
# Then multiplies elements from the end of list nums directly to the created list
# Time Complexity : O(2n) = O(n) / 162ms(71.98%)
# Memory Complexity : O(n) / 20.7MB(80.75%)

class Solution(object):
    def productExceptSelf(self, nums):
        result = []

        # from the front of the nums
        p = 1
        for i in range(len(nums)):
            result.append(p)
            p = p*nums[i]

        # from the end of the nums
        p = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] = result[i] * p
            p = p*nums[i]
        
        return result
            

# Create two lists that multipies elements from each end of list nums(pre, suf)
# Multiply the preffix and suffix
# Time Complexity : O(3n) = O(n) / 190ms(14.49%)
# Memory Complexity : O(2n) = O(n) / 23.97MB(7.41%)

class Solution(object):
    def productExceptSelf(self, nums):

        #prefix
        prefixes = []
        pre = 1
        for i in range(len(nums)-1):
            pre = pre*nums[i]
            prefixes.append(pre)
        
        #suffix
        suffixes = []
        suf = 1
        for i in range(len(nums)-1, 0, -1):
            suf = suf*nums[i]
            suffixes.append(suf)
        suffixes = suffixes[::-1]

        #result
        result = []
        for i in range(len(nums)):
            if i == 0:
                result.append(suffixes[0])
            elif i == len(nums)-1:
                result.append(prefixes[i-1])
            else:
                result.append(suffixes[i]*prefixes[i-1])

        return result

# Brute Force
# Time Complexity: O(n2) / Time Limit Exceeded(18/22)

class Solution(object):
    def productExceptSelf(self, nums):
        # Create empty list to contain producted nums
        result = [1] * len(nums)

        # Product each num to result(except nums[i])
        for i, v in enumerate(nums):
            if i == 0:
                temp = [0]+result[i+1:]
                for j, w in enumerate(temp):
                    temp[j] = w * v
                result = [result[0]]+temp[i+1:]
            elif i == len(nums)-1:
                temp = result[:i]+[0]
                for j, w in enumerate(temp):
                    temp[j] = w * v
                result = temp[:i]+[result[i]]                
            else:
                temp = result[:i]+[0]+result[i+1:]
                for j, w in enumerate(temp):
                    temp[j] = w * v
                result = temp[:i]+[result[i]]+temp[i+1:]
            print(temp, result)
        return result
