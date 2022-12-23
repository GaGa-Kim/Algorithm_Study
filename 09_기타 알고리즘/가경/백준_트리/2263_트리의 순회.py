import sys
input = sys.stdin.readline

# 전위 순회
# 동작하지만 메모리 초과
def pre_order(post_order, in_order):
    if len(post_order) == 0:
        return
    elif len(post_order) == 1:
        print(post_order[0], end=' ')
        return
    elif len(post_order) == 2:
        print(post_order[1], post_order[0], end=' ')
        return

    # 후위 순회의 마지막 노드는 루트 노드이므로
    # 이를 이용해 중위 순회에서 루트 노드의 인덱스를 찾음
    root = in_order.index(post_order[-1]) 

    # 중위 순회 왼쪽 서브트리
    in_order_left = in_order[0 : root] 
    # 중위 순회 오른쪽 서브트리
    in_order_right = in_order[root + 1:] 

    # 후위 순회 왼쪽 서브트리
    post_order_left = post_order[:root] 
    # 후위 순회 오른쪽 서브트리
    post_order_right = post_order[root:-1]

    # 처음에 루트 노드 출력
    print(root, end=' ')
    pre_order(post_order_left, in_order_left)
    pre_order(post_order_right, in_order_right)

n = int(input())    
in_order = list(map(int, input().split())) # 중위 순회
post_order = list(map(int, input().split())) # 후위 순회
pre_order(post_order, in_order)