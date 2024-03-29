# 가로 길이가 n, 세로 길이가 2인 직사각형 바닥을
# 세로*가로가 각각 1*2, 2*1, 2*2인 덮개로 채우려고 할 때,
# 바닥을 채우는 모든 경우의 수 구하는 프로그램
# (2*n 바닥을 채우는 방법의 수를 796,796으로 나눈 나머지 출력)

# i) 가로 길이가 i-1까지 덮개로 이미 채워짐 
#       ~> 2*1로만 가능
# ii) 가로 길이가 i-2까지 덮개로 이미 채워짐 
#       ~> 1*2, 2*2 두 가지 가능
# 점화식) ai = ai-1 + (ai-2 * 2)

# n (1 <= n <= 1,000)
n = int(input())

# DP 테이블 초기화
d = [0] * 1001

d[1] = 1
d[2] = 3
for i in range(3, n+1):
    d[i] = ( d[i-1]*1 + d[i-2]*2 ) % 796796

print(d[n])


