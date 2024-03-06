def solution(array, commands):
    answer = []
    
    for element in commands:
        
        co_arr = []
        
        a, b, c = element   
    
        for x in range(a,b+1):
            co_arr.append(array[x-1])
        
        co_arr.sort()
        answer.append(co_arr[c-1])
            
    return answer