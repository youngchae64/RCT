#10039
sum = 0

def score(num):
    
    your_score = 0
    
    if(num>=40):
        your_score = num
    else:
        your_score = 40 
        
    return your_score
        
for i in range(0,5):
    num = int(input())
    
    your_score = score(num)
    
    sum += your_score
    
mean = sum//5
print(mean)