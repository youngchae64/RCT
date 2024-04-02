def solution(brown, yellow):
    total_sum = brown + yellow
    result = []
    
    for i in range(1, yellow+1):
        if(yellow%i) == 0: 
            a = i #세로 
            b = int(yellow/i) #가로 
            brown_total = (2*b+ 2*a +4)
            if a <= b and (a*b + brown_total == total_sum):
                result.append(b+2)
                result.append(a+2)
                return result 

