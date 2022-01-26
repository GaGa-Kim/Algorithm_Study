# 2_개선된 소수의 판별.py
import math

# 소수 판별 함수(2 이상의 자연수에 대하여)
def is_prime_number(x): 
    # 2부터 X의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

print(is_prime_number(4)) # False
print(is_prime_number(7)) # True
