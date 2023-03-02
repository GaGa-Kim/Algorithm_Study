# 24416번
# n의 피보나치 수를 재귀 호출과 동적 프로그래밍으로 구현하고,
# 각 코드의 실행 횟수 출력

# 5 ≤ n ≤ 40
n = int(input())

cnt1 = cnt2 = 0

# 재귀 호출
def fibo_recursive(n):
    global cnt1 
    cnt1 += 1
    if n == 1 or n == 2:
        cnt1 -= 1
        return 1
    else:
        return fibo_recursive(n-1) + fibo_recursive(n-2)

# dp
dp = [0] * (n+1)
dp[1] = dp[2] = 1

for i in range(3, n+1):
    cnt2 += 1
    dp[i] = dp[i-1] + dp[i-2]

fibo_recursive(n)
print(cnt1+1, cnt2)


