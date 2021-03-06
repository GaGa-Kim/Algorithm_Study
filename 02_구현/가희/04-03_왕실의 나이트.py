# 8*8 정원, 특정 위치에 나이트가 있음
# 나이트는 L자 형태로만 이동 가능, 정원 밖으로 못나감

# <이동 방법 2가지>
# 1. 수평으로 두 칸 이동한 뒤 수직으로 한 칸 이동
# 2. 수직으로 두 칸 이동한 뒤 수평으로 한 칸 이동

# 행) 1~8 / 열) a~h
# 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수 출력하는 프로그램

input_data = input() # 열행 ex) a1
row = int(input_data[1])
# ord: 문자->아스키코드, 1~8까지이므로 +1 해줌
col = int(ord(input_data[0])) - int(ord('a')) + 1 

# 나이트 이동 방향 벡터(행, 열): (-2,-1)부터 반시계 방향
# 순서는 상관없긴 함 ㅎㅎ 
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), 
        (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
# 8가지 방향에 대해 이동 가능 여부 확인
for step in steps:
    # 현재 좌표 + 이동 경로 
    nr = row + step[0]
    nc = col + step[1]
    # 8 * 8 좌표 안에 있으면 이동
    if nr >= 1 and nr <=8 and nc >=1 and nc <=8:
        result += 1

print(result)
        