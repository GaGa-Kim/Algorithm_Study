# 3_왕실의 나이트.py
# 현재 나이트의 위치 입력받기
input_data = input() # 예) a1
row = int(input_data[1]) # 열 : 1
column = int(ord(input_data[0])) - int(ord('a')) + 1 # 행 : a - 아스키 코드 변환

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 하나씩 확인 : (-2, -1) 이라면
    next_row = row + step[0] # step[0]은 -2
    next_column = column + step[1] # step[1]은 -1
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_row >= 1 and next_column <= 8:
        result += 1

print(result)