# put string into list
# Time: O(n) / 36.31%
# Space: O(n) / 97.21%
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        output = 0
        jewelsList = []
        for jewel in jewels:
            jewelsList.append(jewel)
        for stone in stones:
            if stone in jewelsList:
                output += 1
        return output 