import sys
input = sys.stdin.readline

n = int(input())
straw = [int(input()) for _ in range(n)]
straw.sort(reverse=True)

isTrue = False
answer = 0
for i in range(n - 2):
    if straw[i] < straw[i + 1] + straw[i + 2]:
        answer = straw[i] + straw[i + 1] + straw[i + 2]
        isTrue = True
        break
if isTrue:
    print(answer)
else:
    print(-1)