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
                # python divsion mechanism has something different with C/C++, 
                # simply j/i will make a mistake in the OJ system
                    num.append(int(j/float(i))
                        
                else:   # in fact this problem should have no else situation.
                    raise Exception('Not a number or operator')
                    
        return num.pop()
