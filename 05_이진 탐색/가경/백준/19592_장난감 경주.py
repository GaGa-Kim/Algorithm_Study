# 부스터를 사용했을 때의 경주 시간
def booster(v, bv):
    distance = x - bv
    return (distance / v) + 1

t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    speed = list(map(int, input().split()))
    winner = max(speed)
    # 부스터를 쓰지 않고 단독 우승이 가능한 경우
    if speed.count(winner) == 1 and speed[n - 1] == winner:
        print(0)
        continue
    else:
        # 경주 시간
        time = x / winner

        start, end = 0, y
        # 부스터 속도 이진 탐색
        while start <= end:
            mid = (start + end) // 2
            boost = booster(speed[-1], mid)
            # 부스터를 사용하지 않은 참가자보다 시간이 더 오래 걸릴 경우, 부스터 속도 증가
            if boost >= time:
                start = mid + 1
            # 부스터를 사용하지 않은 참가자보다 시간이 더 빠를 경우, 부스터 속도 감소
            else:
                end = mid - 1
        # 부스터 한계치를 사용해야만 우승이 가능하다면, 단독 우승 불가
        if start > y:
            print(-1)
        # 단독 우승을 위해 부스터를 사용해서 이동해야하는 최소한의 거리
        else:
            print(start)
