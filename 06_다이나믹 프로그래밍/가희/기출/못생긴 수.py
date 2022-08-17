# n번째 못생긴 수 찾는 프로그램

# 못생긴 수) 2, 3, 5만을 소인수로 가지는 수
# 1도 못생긴 수라고 가정

# 못생긴 수에 2, 3, 5를 곱한 값도 못생긴 수에 해당함
# => 각 못생긴 수에 대해 2의 배수, 3의 배수, 5의 배수를 고려

# 1 <= n <= 1,000
n = int(input())

# dp 테이블
ugly = [0] * n 
ugly[0] = 1 # 1은 못생긴 수

# 2배, 3배, 5배를 위한 인덱스
i2 = i3 = i5 = 0
# 처음에 곱셈값을 초기화
next2, next3, next5 = 2, 3, 5

# 1 ~ n 못생긴 수 찾기
for i in range(1, n):
    # 가능한 곱셈 결과 중에서 가장 작은 수 선택
    ugly[i] = min(next2, next3, next5)
    
    # 인덱스에 따라 곱셈 결과 증가
    if ugly[i] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[i] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[i] == next5:
        i5 += 1
        next5 = ugly[i5] * 5

# n번째 못생긴 수 출력
print(ugly[n-1])
    



