import sys
input = sys.stdin.readline

# 후위 순회
def post_order(pre_order, in_order):
    if len(pre_order) == 0:
        return
    elif len(pre_order) == 1:
        print(pre_order[0], end=' ')
        return
    elif len(pre_order) == 2:
        print(pre_order[1], pre_order[0], end=' ')
        return

    # 전위 순회의 첫 번째 노드는 루트 노드이므로
    # 이를 이용해 중위 순회에서 루트 노드의 인덱스를 찾음
    root = in_order.index(pre_order[0]) 

    # 중위 순회 왼쪽 서브트리
    in_order_left = in_order[0 : root] 
    # 중위 순회 오른쪽 서브트리
    in_order_right = in_order[root + 1:] 

    # 전위 순회 왼쪽 서브트리
    pre_order_left = pre_order[1: 1 + len(in_order_left)] 
    # 전위 순회 오른쪽 서브트리
    pre_order_right = pre_order[len(pre_order_left) + 1:]

    # 마지막으로 루트 노드 출력
    post_order(pre_order_left, in_order_left)
    post_order(pre_order_right, in_order_right)
    print(pre_order[0], end=' ')

t = int(input())
for _ in range(t):
    n = int(input())
    pre_order = list(map(int, input().split()))
    in_order = list(map(int, input().split()))

    post_order(pre_order, in_order)
    print()