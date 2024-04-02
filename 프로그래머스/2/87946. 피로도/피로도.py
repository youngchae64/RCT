from itertools import permutations

def solution(k, dungeons):
    
    answer = 0 
    
    for perm in permutations(dungeons, len(dungeons)):
        count = 0 
        hp = k 
        for pe in perm:
            if hp >= pe[0]:
                hp -= pe[1]
                count += 1 
            
            if count > answer:
                answer = count 
            
    return answer