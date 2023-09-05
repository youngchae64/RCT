N = int(input())
array = []

for i in range(N):
    word = input()
    array.append(word)
    
# 중복 제거를 하기 위해 set을 사용한 후, 리스트로 변환
unique_sorted_array = sorted(list(set(array)), key=lambda x: (len(x), x))

for element in unique_sorted_array:
    print(element)