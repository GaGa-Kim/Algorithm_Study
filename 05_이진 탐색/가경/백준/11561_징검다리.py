import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    start, end = 1, n
    while start <= end:
        mid = (start + end) // 2
        # 등차수열
        if mid * (mid + 1) // 2 <= n:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    print(answer)
