word = input()

alpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

count = 0

for a in alpha:
    if a in word:
        count += word.count(a)
        
length = len(word)

sum = length - count 

print(sum)
