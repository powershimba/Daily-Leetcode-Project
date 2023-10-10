class Solution(object):
    def dailyTemperatures(self, temperatures):
        

"""
:type temperatures: List[int]
:rtype: List[int]
"""


"""
# Iterative
# Time : O(n2) / Time Limit Exceeded (33/48)
class Solution(object):
    def dailyTemperatures(self, temperatures):
        result = []
        for i in range(len(temperatures)):
            cnt = 0
            char = temperatures[i]
            for j in range(i+1, len(temperatures)):
                cnt += 1   
                if temperatures[j] > char:
                    result.append(cnt)
                    break
                elif j == len(temperatures) - 1:
                    result.append(0)
                    
        result.append(0)
        return result
"""