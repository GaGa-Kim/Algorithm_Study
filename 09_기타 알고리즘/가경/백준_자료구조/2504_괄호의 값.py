import sys
input = sys.stdin.readline

parentheses = list(input().rstrip())
stack = []
answer = 0
tmp = 1
for i in range(len(parentheses)):
    # (
    if parentheses[i] == '(':
        stack.append(parentheses[i])
        tmp *= 2 # 값은 2 * tmp
    # [
    elif parentheses[i] == '[':
        stack.append(parentheses[i])
        tmp *= 3 # 값은 3 * tmp
    # )
    elif parentheses[i] == ')':
        # [)는 올바르지 못한 괄호열
        if not stack or stack[-1] == '[':
            answer = 0
            break
        # ()
        if parentheses[i - 1] == '(':
            answer += tmp
        stack.pop()
        tmp //= 2
    # ]
    else:
        # (]는 올바르지 못한 괄호열
        if not stack or stack[-1] == '(':
            answer = 0
            break
        # []
        if parentheses[i - 1] == '[':
            answer += tmp
        stack.pop()
        tmp //= 3
if stack:
    print(0)
else:
    print(answer)