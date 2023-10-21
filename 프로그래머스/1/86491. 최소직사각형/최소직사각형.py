def solution(sizes):
    
    w = []
    h = []
    
    for row in sizes:
        w.append(max(row))
        h.append(min(row))
        
    return max(w)*max(h)