#25305

N,k = map(int,input().split())

input_string = input()

numbers = input_string.split()

numbers = [int(num) for num in numbers]

new = sorted(numbers, reverse=True)

print(new[k-1])