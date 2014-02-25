class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        num = []
        for token in tokens:
            try:
                num.append(int(token))
            except ValueError:
                if (token == '+'):
                    num.append(num.pop() + num.pop())
                elif (token == '*'):
                    num.append(num.pop() * num.pop())
                elif (token == '-'):
                    i = num.pop()
                    j = num.pop()
                    num.append(j - i)
                elif (token == '/'):
                    i = num.pop()
                    j = num.pop()
                    if (i*j < 0):
                        if (i<0):
                            i = -i
                        else:
                            j = -j
                        num.append(0-j/i)
                    else:
                        num.append(j/i)
                else:
                    raise Exception('Not a number or operator')
        return num.pop()
