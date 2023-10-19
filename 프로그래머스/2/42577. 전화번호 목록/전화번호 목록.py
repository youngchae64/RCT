def solution(phone_book):
    
    #sort() 메서드는 원본 리스트를 정렬하고 None을 반환
    # phone_book = phone_book.sort() 는 None 
    phone_book.sort() #이건 그냥 정렬 
    
    #answer = True 
    
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            #answer = False
            return False
        
    return True