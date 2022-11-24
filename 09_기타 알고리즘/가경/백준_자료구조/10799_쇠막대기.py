import sys
input = sys.stdin.readline

bar = list(input().rstrip())
stack = []
answer = 0
for i in range(len(bar)):
    # (
    if bar[i] == '(':
        stack.append('(')
    # )
    else:
        # ()는 레이저
        if bar[i - 1] == '(':
            stack.pop()
            answer += len(stack)
        # ))는 쇠막대기의 오른쪽 끝
        else:
            stack.pop()
            answer += 1
print(answer)

