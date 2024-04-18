import heapq as hq 

def solution(scoville, K):
    
    hq.heapify(scoville)
    answer = 0 
    
    while scoville[0] < K :
        
        if len(scoville) < 2:
            return -1 
        
        first = hq.heappop(scoville)
        second = hq.heappop(scoville)
        
        new = hq.heappush(scoville, first + second*2)
        
        answer += 1
        
        if scoville[0] >= K:
            break 
        
    return answer 