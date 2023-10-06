#2798

from itertools import combinations 

card_num, target_num = map(int,input().split())
card_list = list(map(int,input().split()))
biggest_num = 0

for cards in combinations(card_list,3):
    temp_num = sum(cards)
    if biggest_num < temp_num <=target_num:
        biggest_num = temp_num 
        
print(biggest_num )