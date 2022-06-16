# 2606번
# 1번 컴퓨터가 웜 바이러스에 걸렸을 때,
# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터 수 출력하는 프로그램
# dfs 풀이

import sys
input = sys.stdin.readline

# 컴퓨터의 수(<=100)
n = int(input())

# 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수
m = int(input())

# 컴퓨터 연결 정보
conn = [ [] for _ in range(n+1) ]
for _ in range(m):
    a, b = map(int, input().split())
    conn[a].append(b)
    conn[b].append(a) # 서로 연결되어 있으므로

result = 0    

def dfs(v):
    global result
    visited[v] = True
    for i in conn[v]:
        if not visited[i]:
            dfs(i)
            result += 1

visited = [False] * (n+1)
dfs(1)
print(result)       