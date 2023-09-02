"""
1342. Number of Steps to Reduce a Number to Zero

Given an integer num, return the number of steps to reduce it to zero.
In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
"""


"My Solution (Runtime: 18ms)"
class Solution(object):
    def numberOfSteps(self, num):

        count = 0
        while(num != 0):
            if num % 2 == 0:
                num = num/2
                count += 1
            else:
                num = num-1
                count += 1

        return count

"""
Other Solution 1 : Bitwise (Runtime: 3ms)

class Solution(object):
    def numberOfSteps(self, num):
        count = 0
        while(num>0):
            if num & 1 == 0:
                num = num >> 1
                count += 1
            else:
                num = num - 1
                count += 1
        return count

Other Solution 2 : Recursive + Bitwise (Runtime: 14 ms)

class Solution(object):
    def numberOfSteps(self, num):
        if num == 0:
            return 0
        elif num & 1 == 0:
            num = num >> 1
        else: 
            num = num - 1
        return 1 + self.numberOfSteps(num)


"""