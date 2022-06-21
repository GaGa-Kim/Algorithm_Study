# 백준 2644번
# 주어진 두 사람의 촌수를 계산하는 프로그램
# bfs 풀이

# 자식을 트리의 시작노드, 부모를 자식 노드로 놓고 순회,
# 자식노드(부모)에 도착하는 경우 부모노드(자식)가 갖는 촌수 + 1

import sys
input = sys.stdin.readline
from collections import deque

# 전체 사람 수 n (1 <= n <= 100)
n = int(input())

# 촌수를 계산해야 하는 서로 다른 두 사람의 번호
a, b = map(int, input().split())

# 부모 자식들 간의 관계의 개수 m
m = int(input())

# 부모 자식 간 관계 (x,y) ~ (부모, 자식)
# 각 사람의 부모는 최대 한 명만 주어짐
graph = [ [] for _ in range(n+1) ]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

    
def bfs(v):
    q = deque([v])
    visited[v] = True
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                result[i] = result[now] + 1
                visited[i] = True
                q.append(i)
            
            
visited = [False] * (n+1)    
result = [0] * (n+1)
bfs(a) # 자식을 트리의 시작노드로

if result[b] > 0:
    print(result[b])    
else: # 친척 관계가 없는 경우 -1 출력
    print(-1)
