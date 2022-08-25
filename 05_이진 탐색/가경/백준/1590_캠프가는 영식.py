n, t = map(int, input().split())
result = []
for _ in range(n):
    s, l, c = map(int, input().split())
    # 버스 도착 시간 리스트
    bus = [s + l * i for i in range(c)]
    # 마지막 버스 시간보다 영식이가 늦을 경우
    if bus[-1] < t:
        continue

    j = 0
    start, end = 0, c - 1
    while start <= end:
        mid = (start + end) // 2
        # 버스 도착 시간이 영식이보다 느릴 경우
        if bus[mid] >= t:
            j = mid
            end = mid - 1
        # 버스 도착 시간이 영식이보다 빠를 경우
        else:
            start = mid + 1
    # 버스 별로 기다려야 하는 시간 추가
    result.append(bus[j] - t)

if len(result) == 0:
    print(-1)
else:
    print(min(result))