
def solution(participant, completion):
    
    answer = ''
    hash_dict = {}
    sumHash = 0 
    hashed_value = 0
    
    for i in participant:
        hashed_value = hash(i) #선수 이름의 해시값을 계산 
        hash_dict[hashed_value] = i #계산된 hash값을 키로 사용하여 이름을 딕셔너리에 저장 
        sumHash += hashed_value 
        
    for j in completion:
        hashed_value = hash(j) #완주한 선수 이름의 해시값을 계산 
        sumHash -= hashed_value #완주한 선수의 해시값을 총합에서 빼준다 
        
    return hash_dict[sumHash] 
        
            