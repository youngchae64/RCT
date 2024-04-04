def solution(progresses, speeds):
    
    days = []
    result = []
    
    for i in range(0,len(progresses)):
        count = 0 
        total = progresses[i]
        
        while True:
            total += speeds[i]
            count +=1 
            if(total >= 100):
                days.append(count)
                break
    
    cnt = 1 
    for j in range(0,len(days)-1): 
        if days[j] >= days[j+1]:
            days[j + 1] = days[j] 
            cnt += 1       
        else:
            result.append(cnt)
            cnt = 1
    result.append(cnt)
            
    return result 
            
             
            
            
            
