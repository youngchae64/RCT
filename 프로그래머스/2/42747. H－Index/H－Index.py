def solution(citations):
    

    
    citations.sort(reverse = True)
    arr = list(enumerate(citations))
    
    
    for a,b in arr:
        if a+1 > b:
            return a
        
    return len(citations)