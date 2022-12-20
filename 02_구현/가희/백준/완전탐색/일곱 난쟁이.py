# 2309번
# 아홉 난쟁이의 키가 주어졌을 때, 백설공주를 도와 일곱 난쟁이를 찾는 프로그램

# 일곱 난쟁이의 키 합은 100 

from itertools import combinations

# 1<= 난쟁이 키 <= 100
heights = [int(input()) for _ in range(9)]

for i in list(combinations(heights, 7)):
    if sum(i) == 100:
        print(*sorted(i), sep='\n')
        break
