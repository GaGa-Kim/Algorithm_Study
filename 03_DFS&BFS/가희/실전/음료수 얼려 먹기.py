# n x m 크기의 얼음 틀 모양이 주어졌을 때 생성되는 총 아이스크림의 개수 구하는 프로그램
# 구멍: 0, 칸막이: 1
# 구멍이 뚫려있는 부분끼리 상하좌우로 붙어있는 경우, 서로 연결된 것으로 간주

# 1. 특정한 지점의 주변 상하좌우를 살펴본 뒤에 주변 지점 중에서 값이 0이면서 
#   아직 방문하지 않은 지점이 있다면 해당 지점 방문
# 2. 방문한 지점에서 다시 상하좌우를 살펴보면서 방문을 다시 진행하면, 연결된 지점 모두 방문 가능

# 얼음 틀 세로 n, 가로 m (1 <= n,m <= 1,000)
n, m = map(int, input().split())

# 얼음 틀 형태
graph  = [list(map(int, input())) for _ in range(n)]

# dfs로 특정한 노드 방문 뒤에 연결된 모든 노드들 방문
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1 # 방문 처리
        # 상하좌우 위치도 모두 재귀적 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

# 모든 노드에 대해 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True: 
            result += 1

print(result)
