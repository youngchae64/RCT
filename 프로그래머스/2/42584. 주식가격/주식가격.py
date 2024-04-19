from collections import deque 

def solution(prices):
    
    max_num = max(prices)
    min_num = min(prices)
    
    answer = []
    #if 지금 원소값이 min이면 len(prices) - (현재 index + 1)
    #elif prices의 현재 원소값과 다음 원소값들을 비교해서 다음원소값중 하나가 지금 원소값보다
    #작으면 그 원소 index - 현재 원소 index array에 저장 
    #마지막 원소는 무조건 0 리턴 
    
    for i in range(len(prices)):
        cnt=0
        for j in range(i+1, len(prices)):
            if prices[j]<prices[i]:
                cnt+=1
                break
            cnt+=1
        answer.append(cnt)

    
    return answer