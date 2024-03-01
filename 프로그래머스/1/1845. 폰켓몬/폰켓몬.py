def solution(nums):
    length = len(nums)/2 #뽑아야 하는 폰켓몬 마리 수 
    set_nums = len(set(nums)) # 중복을 제거한 집합 생성하고 그 집합의 길이 
    
    if(length < set_nums):
        return length
    else:
        return set_nums 
