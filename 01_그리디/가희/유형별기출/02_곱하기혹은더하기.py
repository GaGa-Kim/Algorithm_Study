# 각 자릿수가 0~9로 이루어진 문자열 S
# 왼쪽부터 확인하며 숫자 사이에 '*' 혹은 '+' 연산자를 넣어 만들 수 있는
# 가장 큰 수(20억 이하 정수) 구하는 프로그램

# 단, 무조건 연산은 왼 ~> 오 (곱셈 우선 연산 없음)

# 1 <= 문자열 S의 길이 <= 20
s = list(map(int, input()))

# 첫 번째 숫자
result = s[0]

for i in range(1, len(s)):
    if s[i]<=1 or result<=1:
        result += s[i]
    else:
        result *= s[i]
    
print(result)