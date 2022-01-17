# 5_유클리드 호제법.py
def gcd(a, b):
    if a % b == 0: # A가 B의 배수라면 B를 반환
        return b
    else:
        return gcd(b, a % b) # B와 A를 B로 나눈 나머지(R)의 최대공약수 반환

print(gcd(192, 162)) # 6