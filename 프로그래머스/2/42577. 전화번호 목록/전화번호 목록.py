def solution(phone_book):
    
    phone_book.sort()
    
    num = len(phone_book) # num == 4 , 0 1 2 3 
    
    answer = True 
    #num -1 == 3 
    for i in range(0,num - 1): #0,1,2,
        if(len(phone_book[i])<len(phone_book[i+1])):
            if(phone_book[i+1][:len(phone_book[i])] == phone_book[i]):
                answer = False
                break 
                
    return answer