def plusOne(digits):
    num = sum(digit*pow(10,i) for (i,digit) in zip(range(len(digits)),digits[::-1]))
    return [int(n) for n in str(num+1)]
