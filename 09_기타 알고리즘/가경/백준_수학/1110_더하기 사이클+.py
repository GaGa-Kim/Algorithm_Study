n = input()
number = n
count = 0

while True:
    if len(number) == 1:
        number = "0" + number
    # 26
    # 6 + (2 + 6) = 68
    number = number[-1] + str(int(number[0]) + int(number[1]))[-1]
    count = count + 1
    # 원래 수로 돌아올 때까지 반복
    if (number == n):
        print(count)
        break