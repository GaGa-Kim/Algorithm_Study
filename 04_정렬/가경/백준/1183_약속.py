n = int(input())
t = []
for _ in range(n):
    a, b = map(int, input().split())
    t.append(a - b)

t = sorted(t)
# 홀수일 때
if n % 2 == 1:
    print(1)
# 짝수일 때
else:
    result = t[n // 2] - t[n // 2 - 1] + 1
    print(result)
