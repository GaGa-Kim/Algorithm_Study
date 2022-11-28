import sys
input = sys.stdin.readline

n = int(input())
tops = list(map(int, input().split()))
stack = []
result = []

for i in range(n):
    # 스택이 비어있지 않다면
    while stack:
        # 스택의 맨 윗부분 탑의 높이가 지금 들어오는 탑의 높이보다 클 경우
        if stack[-1][1] > tops[i]:
            # 스택의 맨 윗부분 탑이 수신 가능
            result.append(stack[-1][0] + 1)
            break
        # 스택의 맨 윗부분 탑의 높이가 지금 들어오는 탑의 높이보다 작거나 같을 경우
        else:
            # 수신할 수 없는 탑이므로 빼줌
            stack.pop()
    # 스택이 비어있다면
    if not stack:
        # 수신할 탑이 없으므로  0
        result.append(0)
    stack.append([i, tops[i]])

print(' '.join(map(str, result)))