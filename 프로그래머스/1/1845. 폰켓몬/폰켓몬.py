def solution(nums):
    length = len(nums)/2
    set_nums = len(set(nums))
    
    if(length < set_nums):
        return length
    else:
        return set_nums 
