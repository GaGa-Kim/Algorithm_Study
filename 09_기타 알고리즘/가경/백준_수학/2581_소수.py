m = int(input())
n = int(input())
result = []
for i in range(m, n + 1):
    count = 0
    # 1은 소수가 아님
    if i == 1:
        continue
    for j in range(2, i + 1):
        if i % j == 0:
            count += 1
    # 1을 제외한 자기 자신으로만 나누어 떨어질 때 소수
    if count == 1:
        result.append(i)
if len(result) > 0:
    print(sum(result))
    print(min(result))
else:
    print(-1)