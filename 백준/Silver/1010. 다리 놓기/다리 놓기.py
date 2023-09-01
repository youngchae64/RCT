from math import factorial
from itertools import combinations

def bridge(r,n):
    
    factorial_result = 1
    r_result = 1
    k_result = 1
    
    for i in range(2, n + 1):
        factorial_result *= i
        
    for j in range(1, (n-r) +1 ):
        r_result *= j 
        
    for k in range(1, r+1 ):
        k_result *= k
        
    total = factorial_result / (r_result*k_result)
    return int(total)
    
T = int(input())

for i in range(T):
    num1, num2 = map(int,input().split()) 
    result = bridge(num1, num2)
    print(result)