import sys
input = sys.stdin.readline

a, b = map(int, input().split())
result = 1
while(b != a):
    result += 1
    temp = b
    # b의 끝이 1이라면(나머지가 1) 끝의 1을 뺌
    if b % 10 == 1:
        b //= 10
    # b가 짝수인 경우 2로 나누어줌
    elif b % 2 == 0:
        b //= 2
    # 1을 빼거나 2로 나누는 경우가 되지 않을 경우, 만들 수 없으므로 -1
    if temp == b:
        print(-1)
        break
else:
    print(result)

