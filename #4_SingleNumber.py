class Solution:
    # @param A, a list of integer
    # @return an integer
    
    def singleNumber(self, A):
      # define a set s
        s = set()
        for num in A:
        # check if an integer were in s. 
        # Add if it is not in s, remove if it has been in.
            if num not in s:
                s.add(num)
            else:
                s.remove(num)
        # return the last single number in s
        for item in s:
            return item
