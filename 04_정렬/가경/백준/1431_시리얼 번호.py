n = int(input())
serial = []

# 시리얼번호의 숫자인 것만 더할 때
def sum_num(input):
    result = 0
    for i in input:
        if i.isdigit():
            result += int(i)
    return result

for _ in range(n):
    serial.append(input())

# 길이 순, 숫자 합 순, 사전 순
serial.sort(key = lambda x:(len(x), sum_num(x), x))
for i in serial:
    print(i)