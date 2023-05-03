# 백준 1940번


# 재료 개수 (1 ≤ N ≤ 15,000)
n = int(input())
# 갑옷 만드는데 필요한 수(1 ≤ M ≤ 10,000,000)
m = int(input())

data = list(map(int, input().split()))
data.sort()

start, end = 0, n-1
cnt = 0

while start < end:
    tmp = data[start] + data[end]
    if tmp > m:
        end -= 1
    elif tmp < m:
        start += 1
    else:           # tmp == m
        cnt += 1
        start += 1
        end -= 1
        

print(cnt)
