def solution(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score = [0,0,0]
    for idx,answer in enumerate(answers):
        if answer == pattern1[ idx % len(pattern1)]:
            score[0] += 1 
        if answer == pattern2[idx %len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx % len(pattern3)]:
            score[2] += 1
            
    max_score = max(score)
    
    return [i+1 for i, person in enumerate(score) if person == max_score]
            
        