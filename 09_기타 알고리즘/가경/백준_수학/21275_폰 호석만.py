import sys
input = sys.stdin.readline

# x(int)진수 num(str)을 10진수(int)로 변환
def to_decimal(num: str, x: int) -> int:
    tmp, answer = 0, 0
    # 각 자리별로 진수를 곱하여 10진수로 변환을 반복
    for i in range(len(num)):
        # 숫자라면
        if num[i].isdigit():
            tmp = int(num[i])
        # 문자라면
        else:
            tmp = ord(num[i]) - 97 + 10
        # 한 자리의 값이 x진수에서 나올 수 없는 수이면 -1 리턴
        if tmp >= x:
            return -1
        answer += (x ** (len(num) - i - 1)) * tmp
    return answer

A, B = input().split()

A_decimals, B_decimals = [-1, -1], [-1, -1]
# 10진수로 변환한 값들을 구하여 저장
for i in range(2, 37):
    A_decimals.append(to_decimal(A, i))
    B_decimals.append(to_decimal(B, i))

result = []
for i in range(2, 37):
    for j in range(2, 37):
        # A ≠ B
        if i == j:
            continue
        # 진수 변환한 값들이 같을 때
        if A_decimals[i] != -1 and A_decimals[i] == B_decimals[j]:
                result.append((A_decimals[i], i, j))

if len(result) > 1:
    print('Multiple')
elif not result:
    print('Impossible')
else:
    print(*result[0], sep=' ')