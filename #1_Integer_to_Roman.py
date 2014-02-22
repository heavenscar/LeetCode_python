# Integer to Roman
# Given an integer, convert it to a roman numeral.
# Input is guaranteed to be within the range from 1 to 3999.
# 
# 2014.2.21

class Solution:
    # @return a string
    def intToRoman(self, num):
    
        # Initialize a list to store the mapping relationship between int and roman
        
        Set = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
            ]
       
        roman = ''   
        
        # Match the two types of numbers
        
        for key in Set:                    
            while (num >= key[0]):
                roman += key[1]
                num -= key[0]
       
        return roman
