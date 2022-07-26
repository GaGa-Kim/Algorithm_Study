# 1) 간단한 방법
# 숫자 X를 2부터 X-1까지의 모든 수로 나누어보는 것
def is_prime_number(x):
    # 2부터 (x-1)까지의 모든 수 확인
    for i in range(2, x):
        if x % i == 0:
            return False # 소수 아님
    return True # 소수

#------------------------------------------------
# 2) 자연수의 약수가 가지는 특징 이용
# 가운데 약수를 기준으로 대칭적인 형태
# => 가운데 약수까지만 나누어떨어지는지 확인하면 됨
#    = 제곱근까지만 확인하면 됨

import math

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True
