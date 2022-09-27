import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    parentheses = input()
    count = 0
    for i in parentheses:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        if count < 0:
            print('NO')
            break
    if count > 0:
        print('NO')
    elif count == 0:
        print('YES')

