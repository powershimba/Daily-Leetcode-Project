"""383. Ransom Note  
Given two strings ransomNote and magazine, 
return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

"""

# My Solution
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        list_magazine = []
        for char in magazine:
            list_magazine.append(char)

        for char in ransomNote:
            if char not in list_magazine:
                return False
            else :
                list_magazine.remove(char)
    
        return True

        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        

# Other Solution
from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        str1, str2 = Counter(ransomNote), Counter(magazine)
        return str1 & str2 == str1