import sys
input = sys.stdin.readline

n, m = map(int, input().split())
b = [] # 패키지 가격
p = [] # 낱개 가격
for _ in range(m):
    l, m = map(int, input().split())
    b.append(l)
    p.append(m)

b_min = min(b)
p_min = min(p)

# 6개 기준으로 패키지가 더 저렴할 경우
if b_min < p_min * 6:
    # 패키지로 사고 남은 낱개의 개수와 패키지의 가격을 비교해서 패키지 가격이 더 저렴할 경우
    if b_min < (n % 6) * p_min:
        print((n // 6) * b_min + b_min)
    # 낱개 가격이 더 저렴할 경우
    else:
        print((n // 6) * b_min + (n % 6) * p_min)
# 6개 기준으로 낱개가 더 저렴할 경우
elif b_min >= p_min * 6:
    print(n * p_min)