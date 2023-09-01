#1676

from math import factorial

def find_zero(num):
    facto = factorial(num)
    facto_string = str(facto)
    total = 0
 
    
    for element in reversed(facto_string):
        if(element != '0'):
            break 
        else:
            total += 1 
    return total 
    
N = int(input())

result = find_zero(N)

print(result)