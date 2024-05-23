def solution(phone_book):
    
    #배열 사전순으로 정렬 
    phone_book.sort()
    
    for i in range(len(phone_book) -1):
        word = phone_book[i]
        #첫번째 원소부터 길이 구하고 
        length = len(phone_book[i])
        new_word = phone_book[i+1]
        if(word == new_word[0:length]): #new_word[start:end] start는 포함되지만 end는 미포함
            return False 
        else:
            pass
    return True 