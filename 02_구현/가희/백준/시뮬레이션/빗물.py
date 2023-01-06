# 14719번
# 2차원 세계에 블록이 쌓여있고, 블록 사이에 빗물이 고일 때
# 빗물의 총량을 구하는 프로그램
# - 블록 내부의 빈 공간이 생길 수 없으며, 바닥은 항상 막혀있음
# - 한 칸의 용량은 1


# 양쪽에 더 높은 블록이 존재하면 빗물 고임
# -> 현재 블록의 왼쪽 값 중 최대높이, 오른쪽 값 중 최대 높이를 구해서
# 그 두 값 중 작은 값이 현재 블록 높이보다 크다면, 
# 작은 값 - 현재 블록 높이를 result에 더해줌

# 2차원 세계의 세로 길이 h, 가로 길이 w 
# (1 ≤ h, w ≤ 500)
h, w = map(int, input().split())

# 블록이 쌓인 높이 (0이상 h이하 정수)
block = list(map(int, input().split()))

result = 0
# 첫 번째 블록과 마지막 블록에는 빗물이 고일 수 없으므로 1 ~ w-1
for i in range(1, w-1):
    left = max(block[ :i])
    right = max(block[i+1:])
    tmp = min(left, right)
    
    if block[i] < tmp:
        result += tmp-block[i]

print(result)
