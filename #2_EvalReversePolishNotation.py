class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        num = []
        for token in tokens:
        # if token is an integer, push it into num, else it should be a operator.    
            try:    
                num.append(int(token))
                
            except ValueError:
                if (token == '+'):  
                # handle "+" operator, pop the last two number in the stack, do operation.
                    num.append(num.pop() + num.pop())
                
                elif (token == '*'):    
                # handle "*" operator
                    num.append(num.pop() * num.pop())
               
                elif (token == '-'):    
                # handle "-" operator
                    i = num.pop()
                    j = num.pop()
                    num.append(j - i)
                
                elif (token == '/'):    
                # handle "/" operator.
                    i = num.pop()
                    j = num.pop()
                    
                    if (i*j < 0):   
                    # in the LeetcodeOJ, 6/(-132)should be zero while in python interpreter the result is -1.
                        if (i<0):
                            i = -i
                        else:
                            j = -j
                        num.append(0-j/i)
                    else:
                        num.append(j/i)
                        
                else:   # in fact this problem should have no else situation.
                    raise Exception('Not a number or operator')
                    
        return num.pop()
