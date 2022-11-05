import sys
input = sys.stdin.readline

k = int(input())
number = list(map(int, input().split()))
tree = [[] for _ in range(k)]

# 중위 순회
def in_order(number, level):
    mid = len(number) // 2
    tree[level].append(number[mid])
    if len(number) == 1:
        return
    in_order(number[:mid], level + 1) # 왼쪽 트리
    in_order(number[mid + 1:], level + 1) # 오른쪽 트리

in_order(number, 0)
for i in tree:
    print(*i)