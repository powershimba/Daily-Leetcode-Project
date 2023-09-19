"""
49. Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""

class Solution(object):
    def groupAnagrams(self, strs):
        # create default dict
        anagrams = collections.defaultdict(list)

        for word in strs:
            # sort word(str) -> join chars
            sorted_word = "".join(sorted(word))

            # append to dict
            anagrams[sorted_word].append(word)

        # return values
        return anagrams.values()