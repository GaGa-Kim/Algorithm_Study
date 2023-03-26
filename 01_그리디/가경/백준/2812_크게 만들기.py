import sys
input = sys.stdin.readline

n, k = map(int, input().split())
numbers = input().rstrip()
kk, stack = k, []
for number in numbers:
    # 다음 숫자가 stack에 있는 숫자보다 크면 꺼내서 가장 큰 숫자를 앞쪽에 위치
    while stack and stack[-1] < number and kk > 0:
        stack.pop()
        kk -= 1
    stack.append(number)
print(''.join(stack[:n - k]))