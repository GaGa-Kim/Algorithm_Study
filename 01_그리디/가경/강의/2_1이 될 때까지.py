# 1이 될 때까지
# N, K를 공백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())

result = 0

while True:
    # N이 K로 나누어지는 수가 될 때까지 빼기
    target = (n // k) * k # 나누어 떨어지지 않을 경우, K로 나누어지는 가장 가까운 수를 찾음 (N에서 1을 몇 번 빼서 K로 나누어지는 가장 가까운 수가 될 수 있는지 알기 위해서)
    result += (n - target) # 1을 빼는 연산 횟수
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)