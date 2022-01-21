# 1_피보나치 수열 단순 재귀.py
def fibo(x):
    if x == 1 or x == 2: # 함수가 종료되도록 명시
        return 1
    return fibo(x - 1) + fibo(x - 2)

print(fibo(4)) # 3