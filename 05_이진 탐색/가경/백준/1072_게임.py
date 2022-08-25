import sys
input = sys.stdin.readline

x, y = map(int, input().split())
z = (y * 100) // x
# 이미 몇 번 졌으므로 승률이 100%가 될 수 없음
if z >= 99:
    print(-1)
else:
    # 현재까지 한 게임 횟수만큼 게임을 더 할 경우 무조건 z가 변하므로 end를 x로 설정
    start, end = 1, x
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        # 승률이 오르지 않았을 경우
        if (y + mid) * 100 // (x + mid) <= z:
            start = mid + 1
        else:
            answer = mid
            end = mid - 1
    print(answer)
