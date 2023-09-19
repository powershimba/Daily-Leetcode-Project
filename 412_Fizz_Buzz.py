"""
412. Fizz Buzz

Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
"""

"My Solution"
class Solution(object):
    def fizzBuzz(self, n):
            
        """
        :type n: int
        :rtype: List[str]
        """
        output = []
        for i in range(1,n+1):
            if not i%3 and i%5 :
                output.append("Fizz")
            elif i%3 and not i%5 :
                output.append("Buzz")
            elif not i%3 and not i%5 :
                output.append("FizzBuzz")
            else:
                output.append(str(i))
        return output