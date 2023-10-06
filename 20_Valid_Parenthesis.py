"""
Easy
20. Valid Parentheses
"""

# Mapping
# Time: O(n) / 10ms(90.46%)
# Memory: O(n) / 13.29MB(89.79%)

class Solution(object):
    def isValid(self, s):
        stack = []
        table = {
            ')' : '(',
            '}' : '{',
            ']' : '[',
        }
        for char in s:
            if char not in table: # (, {, [
                stack.append(char)
            elif not stack or (table[char] != stack.pop()): # ), }, ] 
                return False
        return len(stack) == 0

# Iterative
# Time: O(n) / 15ms(55.25%)
# Memory: O(n) / 13.73MB(13.75%)

class Solution(object):
    def isValid(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] =='{' or s[i] =='[':
                stack.append(s[i])
            else:
                if stack != []:
                    last = stack.pop()
                    if (last == '(' and s[i] == ')') or (last == '{' and s[i] == '}') or (last == '[' and s[i] == ']'):
                        continue
                    else:
                        return False
                else:
                    return False
        if stack == []:
            return True 