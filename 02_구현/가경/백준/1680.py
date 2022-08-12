import sys
input = sys.stdin.readline

for _ in range(int(input())):
    w, n = map(int, input().split())
    trash = []
    for _ in range(n):
        x_i, w_i = map(int, input().split())
        trash.append([x_i, w_i])

    capacity = 0 # 쓰레기차 안에 있는 쓰레기 용량
    distance = 0 # 쓰레기차가 이동한 거리
    previous_distance = 0 # 쓰레기차가 이전까지 이동한 거리
    for i in trash:
        # 쓰레기의 양이 쓰레기차의 용량보다 적다면 쓰레기를 싣고 다른 지점으로 감
        if capacity + i[1] < w:
            distance += i[0] - previous_distance
            capacity += i[1]
        # 쓰레기의 양이 쓰레기차의 용량보다 같다면 쓰레기를 싣고 쓰레기장으로 돌아가서 쓰레기를 비우고 다시 돌아옴
        elif capacity + i[1] == w:
            distance += (i[0] - previous_distance) + i[0] * 2
            capacity = 0
            # 만약 이때 더 이상 쓰레기를 실을 지점이 없다면 다시 돌아오지 않음
            if trash.index(i) == n - 1:
                distance -= i[0] * 2
        # 쓰레기의 양이 쓰레기차의 용량보다 크다면 쓰레기를 싣지 않고 쓰레기장으로 돌아가서 쓰레기를 비우고 다시 돌아옴
        elif capacity + i[1] > w:
            distance += (i[0] - previous_distance) + i[0] * 2
            capacity = i[1] # 비우고 다시 돌아와서 쓰레기를 채움
        previous_distance = i[0]
    # 모든 쓰레기 수거 후 다시 쓰레기장으로 돌아감
    if trash.index(i) == n - 1:
        distance += i[0]

    print(distance)