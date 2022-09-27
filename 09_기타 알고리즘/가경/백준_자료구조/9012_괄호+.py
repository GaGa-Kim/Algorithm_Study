import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    parentheses = input()
    stack = []
    for i in parentheses:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack):
                stack.pop()
            else:
                print('NO')
                break
    # break문으로 중료되지 않고 for문이 모두 수행되었을 경우
    else:
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")