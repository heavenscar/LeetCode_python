class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        if not s:
            return 0
        // a generator expression, complicated and handle the problem in one line
        return sum((ord(char)-64)*pow(26,i) for (i,char) in zip(range(len(s)),s[::-1]))
