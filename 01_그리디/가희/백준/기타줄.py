# 1049번
# 끊어진 기타줄의 개수 n과 기타줄 브랜드 m개가 주어지고,
# 각각의 브랜드에서 파는 기타줄 6개가 들어있는 패키지의 가격,
# 낱개로 살 때의 가격이 주어질 때, 적어도 n개를 사기 위해 필요한 돈의 수를 최소로 하는 프로그램


# 1 <= n <= 100, 1 <= m <= 50
n, m = map(int, input().split())

# 각 브랜드의 패키지 가격과 낱개 가격
package = []
piece = []
for _ in range(m):
    a, b = map(int, input().split())
    package.append(a)
    piece.append(b)
    
result = 0
min_package = min(package)
while n > 0:
    if n < 6:
        min_piece = min(piece) * n
        n -= n           
    elif n >= 6:
        min_piece = min(piece) * 6
        n -= 6
    result += min(min_package, min_piece)     
    
print(result)
