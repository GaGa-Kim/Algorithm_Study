import sys
input = sys.stdin.readline

n = int(input())
circle = []
stack = []
for i in range(n):
    x, r = map(int, input().split())
    circle.append((x - r, i)) # x축에 있는 원의 맨 앞 점과 인덱스
    circle.append((x + r, i)) # x축에 있는 원의 맨 뒤 점과 인덱스
circle.sort()

for i in range(n * 2):
    if len(stack) == 0:
        stack.append(circle[i])
    elif stack:
        # 같은 원의 점이라면 (인덱스가 같다면)
        if stack[-1][1] == circle[i][1]:
            stack.pop()
        # 같은 원의 점이 아니라면
        else:
            stack.append(circle[i])
            
# 같은 원의 점끼리 짝을 맞아 모든 스택이 비었다면 조건 만족
if len(stack) == 0:
    print('YES')
# 같은 원의 점끼리 짝이 맞지 않고 겹친다면 조건 불만족
else:
    print('NO')
