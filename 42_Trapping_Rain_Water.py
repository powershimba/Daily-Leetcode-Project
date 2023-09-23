# Two Pointers
# Runtime: 92ms / Memory 14.66MB
class Solution(object):
    def trap(self, height):
        l = 0
        r = len(height) - 1 
        max_l = 0
        max_r = 0
        water = 0

        while l < r:
            if height[l] <= height[r]:
                if max_l < height[l]:
                    max_l = height[l]
                else: 
                    water += max_l - height[l]
                l += 1

            else:
                if max_r < height[r]:
                    max_r = height[r]
                else:
                    water += max_r - height[r]
                r -= 1
        return water

# Brute Force
# Time Limit Exceeded

class Solution(object):
    def trap(self, height):
        total = 0
        for i in range(1, len(height)-1):
            max_left = max(height[:i])
            max_right = max(height[i:])
            max_height = min(max_left, max_right)
            if height[i] < max_height:
                water = max_height - height[i]
                total += water

        return total