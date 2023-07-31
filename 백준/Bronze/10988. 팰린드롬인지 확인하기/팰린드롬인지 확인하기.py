word = input()
length = len(word)
length_2 = int(length/2)
count = 0 

for i in range(0, length_2 + 1): # 단어길이/2 만큼 반복 
    l_i = length - (i+1) #마지막 자리는 length - (i+1)
    if(word[i] == word[l_i]): # 같으면 
        count += 1

if(count >= length_2):
    print("1")
else:
    print("0")
    