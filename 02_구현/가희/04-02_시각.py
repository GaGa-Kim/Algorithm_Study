# <--완전탐색 유형-->
# 00시 00분 00초 ~ 23시 59분 59초까지 모든 경우의 수 ~ 86,400가지 < 100만
# => 완전탐색으로 해결 가능

# 정수 N, 0 <= N <= 23
n = int(input())

count = 0 

for i  in range(n+1): # 시) 0 ~ n
    for j in range(60): # 분) 0 ~ 59
        for k in range(60): # 초) 0 ~ 59
            if '3' in str(i)+str(j)+str(k): # 그냥 문자열 형태로 합침
                count += 1

print(count)