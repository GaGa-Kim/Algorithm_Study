n = int(input())
number = n
count = 0

while True:
    # 26
    a = number // 10 # 26 // 10 = 2
    b = number % 10 # 26 % 10 = 6
    c = (a + b) % 10 # (2 + 6) % 10 = 8
    number = (b * 10) + c # (6 * 10) + 8 = 68

    count = count + 1
    # 원래 수로 돌아올 때까지 반복
    if (number == n):
        break
print(count)
