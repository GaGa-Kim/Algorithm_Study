# n의 크기 100억 이상으로 커질 때
# n이 k의 배수가 되도록 효율적으로 한 번에 빼는 방식

n, k = map(int, input().split())
result = 0

while True:
    # (가장 가까운) k로 나누어 떨어지는 수
    target = (n//k)*k
    result += (n-target)  # -1 연산 횟수

    n = target  # 이제 n은 k의 배수
    if n < k:  # 더 이상 나눌 수 없을 때 반복문 탈출
        break
    result += 1  # //k 연산 횟수
    n //= k

# 남은 수(k보다 작아진 n) -1씩
result += (n-1)
print(result)