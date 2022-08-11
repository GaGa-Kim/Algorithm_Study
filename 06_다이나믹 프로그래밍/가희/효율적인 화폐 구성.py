# n가지 화폐를 최소로 이용하여 m원 만들기 (화폐 순서 상관x)

# 금액 i를 만들 수 있는 최소한의 화폐 개수 ~> ai
# 화폐 단위 ~> k

# ai-k를 만드는 방법 존재 o) ai = min(ai, ai-k + 1)
# ai-k를 만드는 방법 존재 x) ai = 10,001 (INF)

# 1 <= n <= 100, 1 <= m <= 10,000
n, m = map(int, input().split())

# 각 화폐의 가치 (<= 10,000)
array = []
for i in range(n):
    array.append(int(input()))

# DP 테이블 초기화 ~ 처음엔 모두 불가능(10,001)으로 초기화
d = [10001] * (m+1) 

d[0] = 0
for i in range(n): # 화폐 단위
    for j in range(array[i], m+1): # 금액
        if d[j-array[i]] != 10001: # (i-k)원 만드는 방법 존재하는 경우
            d[j] = min(d[j], d[j-array[i]]+1)


if d[m] == 10001: 
    # 불가능 할 때는 -1 출력    
    print(-1)
else:
    print(d(m))