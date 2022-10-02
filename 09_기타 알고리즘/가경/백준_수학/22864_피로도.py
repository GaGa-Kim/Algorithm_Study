a, b, c, m = map(int, input().split())
tired = 0
result = 0
if a > m:
    print(0)
else:
    for i in range(24):
        # 한 시간 일하기
        if tired + a <= m:
            tired += a
            result += b
        # 한 쉬간 쉬기
        else:
            if tired - c >= 0:
                tired -= c
            else:
                tired = 0
    print(result)