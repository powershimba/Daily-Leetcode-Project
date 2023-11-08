# Simply Iterate
# Time: O(n) / 64.13%
# Space: O(n) / 97.21%
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        output = 0
        for stone in stones:
            if stone in jewels:
                output += 1
        return output 