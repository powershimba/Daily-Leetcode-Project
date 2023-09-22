# Brute Force
# Runtime: 2148ms / Memory: 14.04MB
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Hash Map
# Runtime: 46ms / Memory: 13.92MB
# memo: for index, value in enumerate(my_list)
class Solution(object):
    def twoSum(self, nums, target):
        hash_map = {} #save value as (number, index)
        for i, num in enumerate(nums):
            hash_map[num] = i
        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in hash_map and hash_map[pair] != i:
                return [hash_map[pair], i]


# Two Pointers From Each End
# Runtime: 47ms / Memory: 14.19MB
class Solution(object):
    def twoSum(self, nums, target):
        # sort first based on value of nums(maintain index)
        new_nums = []
        for i, num in enumerate(nums):
            new_nums.append((num, i))
        new_nums.sort()

        l, r = 0, len(new_nums)-1
        while l < r:
            if new_nums[l][0] + new_nums[r][0] == target:
                return [new_nums[l][1], new_nums[r][1]]
            elif new_nums[l][0] + new_nums[r][0] > target:
                r = r - 1
            elif new_nums[l][0] + new_nums[r][0] < target:
                l = l + 1
    