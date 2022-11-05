import sys
input = sys.stdin.readline

k = int(input())
number = list(map(int, input().split()))
number_idx = 0
tree = [[] for _ in range(k)]

# 중위 순회
def in_order(level):
    global tree, number_idx
    # 마지막 레벨까지 내려가서 올라옴
    if level == k:
        return
    in_order(level + 1)
    tree[level].append(number[number_idx])
    number_idx += 1
    in_order(level + 1)

in_order(0)
for i in tree:
    print(*i)