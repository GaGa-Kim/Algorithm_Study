# 2477번 
# 참외밭에서 자라는 참외의 수를 구하는 프로그램

#  1m^2의 넓이에 자라는 참외 개수를 헤아린 다음,
# 참외밭의 넓이를 구하면 비례식을 이용하여 참외의 총 개수 구함

# 참외밭은 ㄱ-자 모양이거나 
# ㄱ-자를 90도, 180도, 270도 회전한 모양(┏, ┗, ┛ 모양)의 육각형
# 밭의 경계(육각형의 변)는 모두 동서 방향이거나 남북 방향


# 1m^2의 넓이에 자라는 참외의 개수 (1 ≤ K ≤ 20)
k = int(input())

# 육각형의 임의의 한 꼭짓점에서 출발하여 
# 반시계방향으로 둘레를 돌면서 지나는 변의 방향과 길이
# (1 이상 500 이하의 정수, 동: 1, 서: 2, 남: 3, 북: 4)
list = []
maxW, maxW_index = 0, 0 # 가장 큰 사각형의 너비
maxH, maxH_index = 0, 0 # 가장 큰 사각형의 높이
for i in range(6):
    dir, length = map(int, input().split())
    list.append((dir, length))
    # 가로 (동서)
    if list[i][0] == 1 or list[i][0] == 2:
        if maxW < list[i][1]:
            maxW = list[i][1]
            maxW_index = i
    # 세로 (남북)
    elif list[i][0] == 3 or list[i][0] == 4:
        if maxH < list[i][1]:
            maxH = list[i][1]
            maxH_index = i

shortW = 0 # 가장 큰 사각형에서 뺄 사각형의 너비
shortH = 0 # 가장 큰 사각형에서 뺄 사각형의 높이
# 가장 긴 가로변에 인접한 변 2개(=세로변)의 차
shortW = abs(list[(maxW_index-1) % 6][1] - list[(maxW_index+1) % 6][1])
# 가장 긴 세로변에 인접한 변 2개(=가로변)의 차
shortH = abs(list[(maxH_index-1) % 6][1] - list[(maxH_index+1) % 6][1])

print(abs((maxW*maxH) - (shortW*shortH))*k)

        