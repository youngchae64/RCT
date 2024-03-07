def solution(sizes):
        
    for element in sizes:
        if (element[0]<element[1]):
            new = element[0] 
            element[0] = element[1] 
            element[1] = new 
    
    left_elements = [element[0] for element in sizes]
    right_elements = [element[1] for element in sizes]
    
    left_elements.sort(reverse = True)
    right_elements.sort(reverse = True)
    
    longest_width = left_elements[0]
    longest_height = right_elements[0]
    #가장 긴 가로 길이 longest_width 
    #가장 긴 세로 길이 longest_height 
    
    area = longest_width * longest_height 
    
    return area 
