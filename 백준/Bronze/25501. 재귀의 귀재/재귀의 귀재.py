#25501 

T = int(input())


def recursion(s, l, r):
    global count 
    count += 1 
    if l >= r: return 1  #팰린드롬이면 1반환  
    elif s[l] != s[r]: return 0 #l,r인덱스가 같지 않으면 종료 
    else: 
        return recursion(s, l+1, r-1) #인덱스 하나씩 증가해서 재귀함수 호출 

def isPalindrome(s):
    return recursion(s, 0, len(s)-1) #문자열, 첫번째 index, index 


for i in range(T):
    count = 0 
    string = input()
    a = isPalindrome(string)
    print(a, count)
    
