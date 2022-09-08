import sys
input = sys.stdin.readline

n, m = map(int, input().split())
jewel = [int(input()) for _ in range(m)]

start = 1
end = sum(jewel)
result = 0
while start <= end:
    # 보석을 받는 학생의 수
    total = 0
    # 한 사람이 받는 보석 개수 (질투심)
    mid = (start + end) // 2
    for i in jewel:
        # 남은 보석의 수가 0일 때
        if i % mid == 0:
            total += i // mid
        else:
            total += (i // mid) + 1
    if total > n:
        start = mid + 1
    else:
        result = mid
        end = mid - 1
print(result)