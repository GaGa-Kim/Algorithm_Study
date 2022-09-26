# 14916번
# 손님이 2원, 5원으로만 거스름돈 n원을 달라고 할 때,
# 최소 동전의 개수가 몇 개인지 알려주는 프로그램

# 1 <= n <= 100,000
n = int(input())
result = 0 # 동전 최소 개수

while n > 0:
    if n % 5 == 0:
        result += n//5
        break
    n -= 2
    result += 1

if n < 0:
    print(-1)
else:
    print(result)
