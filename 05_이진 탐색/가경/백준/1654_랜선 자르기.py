import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]

start = 1
end = max(lan)
while (start <= end):
    lines = 0
    mid = (start + end) // 2
    for i in lan:
        # 분할된 랜선 수
        lines += i // mid
    if lines >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)