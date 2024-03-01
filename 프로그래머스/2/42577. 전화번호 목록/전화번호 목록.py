def solution(phone_book):
    
    #배열 길이순으로 정렬 
    phone_book.sort()
    
    for i in range(len(phone_book) -1):
        word = phone_book[i]
        #첫번째 원소부터 길이 구하고 
        length = len(phone_book[i])
        new_word = phone_book[i+1]
        if(word == new_word[0:length]):
            return False 
        else:
            pass
    return True 