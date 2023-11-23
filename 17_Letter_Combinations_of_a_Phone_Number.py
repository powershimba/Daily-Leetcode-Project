# 17. Letter Combinations of a Phone Number
# Medium
# Graph, Recursive

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def dfs(index, letters):
            if len(letters) == len(digits):
                output.append(letters)
                return
            
            for i in range(index, len(digits)):
                for j in dict[digits[i]]:
                    dfs(i + 1, letters + j)
        
        if not digits:
            return []

        dict = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        output = []
        
        dfs(0, "")
        return output
        
