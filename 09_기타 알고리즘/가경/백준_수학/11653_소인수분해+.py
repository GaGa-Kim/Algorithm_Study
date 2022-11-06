n = int(input())

# 2부터 1씩 증가시키며 나눠보기
i = 2
while n != 1:
    # 나눠질 경우
    if n % i == 0:
        # 해당 숫자로 나누어질 동안 나누기
        print(i)
        n = n / i
    # 나누어지지 않을 경우 1 증가
    else:
        i += 1