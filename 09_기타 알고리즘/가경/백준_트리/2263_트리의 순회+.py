import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def pre_order(in_order_start, in_order_end, post_order_start, post_order_end):
    if (in_order_start > in_order_end) or (post_order_start > post_order_end):
        return
    
    # 후위 순회의 마지막 노드는 루트 노드
    root = post_order[post_order_end]
    print(root, end=' ')

    # 중위 순회는 루트를 기준으로 왼쪽, 오른쪽 서브트리로 나누어짐
    # 후위 순회의 끝값인 root가 중위 순회의 어느 인덱스에 위치하는지를 이용
    left = position[root] - in_order_start
    right = in_order_end - position[root]

    # 중위 순회 왼쪽 서브트리
    pre_order(in_order_start, in_order_start + left - 1, post_order_start, post_order_start + left - 1)
    # 중위 순회 오른쪽 서브트리
    pre_order(in_order_end - right + 1, in_order_end, post_order_end - right, post_order_end - 1)

n = int(input())    
in_order = list(map(int, input().split())) # 중위 순회
post_order = list(map(int, input().split())) # 후위 순회

# 중위 순회의 값들의 인덱스값을 저장
position = [0] * (n + 1)
for i in range(n):
    position[in_order[i]] = i

pre_order(0, n - 1, 0, n - 1)