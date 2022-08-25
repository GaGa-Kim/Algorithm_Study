t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    d = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 서쪽에 사이트가 1개일 때, 동쪽의 사이트만큼 경우의 수
            if i == 1:
                d[i][j] = j
                continue
            # 서쪽의 사이트와 동쪽의 사이트 개수가 같으면 경우의 수는 1개
            if i == j:
                d[i][j] = 1
            # 서쪽의 사이트 개수가 n, 동쪽의 사이트 개수가 m일 때 경우의 수는 
            # (서쪽에 n, 동쪽에 m - 1) + (서쪽에 n - 1, 동쪽에 n - 1) 
            else:
                if j > i:
                    d[i][j] = d[i][j - 1] + d[i - 1][j - 1]
    print(d[n][m])