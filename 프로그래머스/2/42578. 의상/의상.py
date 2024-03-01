import collections

def solution(clothes):
    answer=1
    #value값 count 
    dict = {}

    #리스트를 딕셔너리로 변환 
    for item, category in clothes:
        if category in dict:
            dict[category] += 1
        else:
            dict[category] = 1 
            
    
    for key,value in dict.items():
        answer*=(value+1)
        
    return answer-1
        
