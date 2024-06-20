N = int(input())

for i in range(1, N + 1):
    split_data = map(int, input().split())

    sum = 0
    for element in split_data:
        number = int(element)
        if number % 2 == 1:
            sum += number
    print("#" + str(i) + " " + str(sum))
