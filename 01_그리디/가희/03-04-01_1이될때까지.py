# 단순한 풀이 _ n <= 100000이라 가능

n, k = map(int, input().split())
result = 0

# n이 k이상이면 계속 k로 나눔
while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

# 남은 수(k보다 작아진 n)에 대해 -1씩
while n > 1:
    n -= 1
    result += 1

print(result)