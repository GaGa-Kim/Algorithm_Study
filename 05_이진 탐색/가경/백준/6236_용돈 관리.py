import sys
input = sys.stdin.readline

n, m = map(int, input().split())
moneys = list(int(input()) for _ in range(n))

start = min(moneys)
end = sum(moneys)
k = 0
while (start <= end):
    mid = (start + end) // 2 # 인출할 금액
    now = mid # 처음 인출 금액 (가진 돈)
    withdraw = 1 # 인출 횟수
    for money in moneys:
        # 돈이 모자라면 인출
        if now < money:
            now = mid
            withdraw += 1
        now -= money
    if withdraw > m or mid < max(moneys):
        start = mid + 1
    else:
        end = mid - 1
        k = mid
print(k)


