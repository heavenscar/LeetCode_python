# Reverse Words In a String
# Given an input string, reverse the string word by word.
# 2014.9.9

class Solution:
    # @param s, a string
    # @return a string
    
    def reverseWords(self, s):
        # Split given string and reverse it. Return the joined list.
        wordList = s.split()[::-1]
        return ' '.join(wordList)
