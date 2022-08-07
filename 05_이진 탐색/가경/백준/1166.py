import sys
input = sys.stdin.readline

n, l, w, h = map(int, input().split())

start, end = 0, max(l, w, h)
for _ in range(10000):
    mid = (start + end) / 2
    # mid에 따라 직육면체에 n개의 정육면체가 모두 들어가는지 확인 (개수는 정수이므로 // 사용)
    if (l // mid) * (w // mid) * (h // mid) >= n:
        start = mid
    else:
        end = mid
print("%.10f" %(end))