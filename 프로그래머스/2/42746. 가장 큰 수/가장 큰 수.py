def solution(numbers):
    
    #numbers 세번 반복하고 정렬 reverse = True로 
    arr = []
    for element in numbers:
        arr.append(str(element))
        
    new_arr = sorted(arr, key = lambda x: 3*x, reverse = True)
    
    answer = ''.join(new_arr)
    
    answer = int(answer)
    answer = str(answer)
    
    return answer
