# 백준 2231번
# 자연수 n이 주어졌을 때, n의 가장 작은 생성자를 구하는 프로그램

# 자연수 n의 분해합) n과 n을 이루는 각 자리수의 합
# 자연수 m의 분해합이 n인 경우, m을 n의 생성자라고 함
# 생성자는 없을 수도, 여러 개일 수도 있음

# 1 <= n <= 1,000,000
n = int(input())

m = 0   # 생성자
for i in range(1, n+1):
    tmp = i + sum(map(int, str(i)))
    
    if tmp == n:
        m = i
        break
print(m)






