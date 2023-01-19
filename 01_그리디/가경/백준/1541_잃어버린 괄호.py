import sys
input = sys.stdin.readline

cal = input().split('-')
number = []
# 덧셈끼리의 연산해주기
for i in cal:
    tmp = 0
    c = i.split('+')
    for j in c:
        tmp += int(j)
    number.append(tmp)

# 최대가 된 덧셈 값으로 뺄셈해주기
result = number[0]
for i in range(1, len(number)):
    result -= number[i]
print(result)