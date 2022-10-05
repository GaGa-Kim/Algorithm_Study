n = int(input())
cow = [-1] * 11
count = 0
for _ in range(n):
    a, b = map(int, input().split())
    # 소가 처음 관찰되었을 경우
    if cow[a] == -1:
        cow[a] = b
    # 소가 두 번째 이상 관찰되었을 경우
    else:
        # 소의 위치가 바뀔 경우
        if cow[a] != b:
            count += 1
            cow[a] = b
print(count)
