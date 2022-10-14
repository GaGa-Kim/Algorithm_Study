now = input().split(':')
future = input().split(':')

if now == future:
    print("24:00:00")
else:
    # 나트륨을 던질 시간이 다음날이면
    if int(now[0]) > int(future[0]):
        future[0] = int(future[0]) + 24
    # 초로 변환
    now_time = int(now[0]) * 3600 + int(now[1]) * 60 + int(now[2])
    future_time = int(future[0]) * 3600 + int(future[1]) * 60 + int(future[2]) 

    time = future_time - now_time
    time_list = []
    time_list.append(int(time // 60 // 60))
    time_list.append(int(time // 60 % 60))
    time_list.append(int(time % 60))

    print("%02d:%02d:%02d" %(time_list[0], time_list[1], time_list[2]))
