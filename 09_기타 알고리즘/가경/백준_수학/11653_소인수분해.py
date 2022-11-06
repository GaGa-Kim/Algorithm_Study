n = int(input())

if n == 1:
    print('')
# 2부터 n까지 나눠보기
for i in range(2, n + 1):
    # 나눠질 경우
    if n % i == 0:
        # 해당 숫자로 나누어질 동안 나누기
        while n % i == 0:
            print(i)
            n = n / i