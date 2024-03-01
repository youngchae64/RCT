import collections 

def solution(participant, completion):
    
    list = participant + completion 
    new_list = collections.Counter(list)
    
    #new_list의 값이 홀수이면 출력
    for key,value in new_list.items():
        if (value%2) == 1:
            return key
            