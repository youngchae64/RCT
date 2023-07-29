s = input()

sum = 0 
blank = 0
len_s = len(s)

for i in range(0,len_s):
        if((s[0] == " ") & (s[-1] == " ")):
            blank += 2
            break
            
        elif((s[-1] == " ")):
            blank += 1 
            break
            
        elif(s[0] == " "):
            blank += 1 
            break 
            
            
for i in range(0,len_s):
    if(s[i] == " "):
        sum += 1
        
word = sum - blank + 1 

print(word)