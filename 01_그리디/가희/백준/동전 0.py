# 11047번
# n 종류의 동전을 많이 가지고 있을 때 동전을 적절히 사용해서 
# 그 가치의 합을 k로 만들려 할 때, 필요한 동전 개수의 최솟값 구하는 프로그램

# 1<= n <= 10, 1 <= k <= 100,000,000
n, k = map(int, input().split())

# 동전의 가치 Aj 
# (1 <= Aj <= 1,000,000, A1 = 1, i >= 2 인 경우 Aj는 Aj-1의 배수)
# ~> 이 조건때문에 그리디 알고리즘 적용 가능
coins = [int(input()) for _ in range(n)]
coins.reverse()

result = 0
for i in coins:
    if i <= k:
        result += k // i
        k = k % i

print(result)
