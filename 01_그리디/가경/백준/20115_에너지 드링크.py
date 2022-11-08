import sys
input = sys.stdin.readline

n = int(input())
drinks = list(map(int, input().split()))
# 내림차순 정렬
drinks.sort(reverse=True)

# 가장 많은 양의 드링크를 최대한 넣을 수 있도록 함
result = drinks[0]
for i in range(1, n):
    result += drinks[i] / 2

print('%g' %result)