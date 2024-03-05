def solution(arr):
    answer = []
    a = 'a'
    arr.append(a)
    length = len(arr) 
    
    for i in range(0, length-1):
        if(arr[i] == arr[i+1]):
            pass
        else:
            answer.append(arr[i])
        
    return answer