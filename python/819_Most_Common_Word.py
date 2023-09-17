class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        paragraph = paragraph.lower()
        for char in ',.':
            paragraph = paragraph.replace(char, "")
        words = paragraph.split()

        dict = {}
        for word in words:
            if word not in banned:
                if word not in dict:
                    dict[word] = 1
                else:
                    dict[word] += 1
        
        max_key = max(dict, key=lambda k: dict[k])
        return max_key

        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        