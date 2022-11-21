import sys
input = sys.stdin.readline

n = int(input())
cal = input().rstrip()
numbers = [0] * n
for i in range(n):
    numbers[i] = int(input())

stack = []
for i in cal:
    # 피연산자를 만났을 때
    if 'A' <= i <= 'Z':
        stack.append(numbers[ord(i) - ord('A')])
    # 연산자를 만났을 때
    else:
        str2 = stack.pop()
        str1 = stack.pop()

        if i == '+':
            stack.append(str1 + str2)
        elif i == '-':
            stack.append(str1 - str2)
        elif i == '*':
            stack.append(str1 * str2)
        elif i == '/':
            stack.append(str1 / str2)

print('%.2f' %stack[0])