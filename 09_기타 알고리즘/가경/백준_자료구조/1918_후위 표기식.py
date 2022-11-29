import sys
input = sys.stdin.readline

cal = list(input().rstrip())
stack = []
result = ''

for i in cal:
    # 피연산자일 경우
    if i.isalpha():
        result += i
    # 연산자일 경우
    else:
        # 우선순위 1. ( )
        if i == '(':
            stack.append(i)
        # 우선순위 2. * /
        elif i == '*' or i == '/':
            # 스택이 맨 뒤 요소가 *와 /일 동안의 모든 연산자들을 result에 추가
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                result += stack.pop()
            stack.append(i)
        # 우선순위 3. + -
        elif i == '+' or i == '-':
            # 스택의 맨 뒤 요소가 (이기 전의 모든 연산자들을 result에 추가
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(i)
        elif i == ')':
            # 스택의 맨 뒤 요소가 (이기 전의 (와 ) 사이에 있는 모든 연산자들을 result에 추가
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()

while stack:
    result += stack.pop()
print(result)
