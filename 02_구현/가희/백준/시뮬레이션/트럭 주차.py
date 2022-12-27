# 2979번
# 주차 요금 A, B, C와 주차 시간이 주어졌을 때, 주차요금을 구하는 프로그램

# 한 대 주차 ~ 1분에 한 대당 A원
# 두 대 주차 ~ 1분에 한 대당 B원
# 세 대 주차 ~ 1분에 한 대당 C원

# 1. 가장 마지막으로 떠난 트럭의 시간을 구한 뒤
# 해당 크기의 리스트(parking) 선언하고 0으로 초기화
# 2. 각 시간대별로 트럭 파킹 정보 입력
#   ex) 5초에 트럭 3대이면 parking[4]=3 
# 3. 주차 요금 계산


# 1 <= c <= b <= a <= 100
a, b, c = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(3)]
lastTime = max(data[0][1], data[1][1], data[2][1])
parking = [0] * (lastTime-1)

for car in data:
    for i in range(car[0]-1, car[1]-1):
        parking[i] += 1
    
result = 0
for i in parking:
    if i == 1:
        result += a
    elif i == 2:
        result += (2 * b)
    elif i == 3:
        result += (3 * c)

print(result)
    