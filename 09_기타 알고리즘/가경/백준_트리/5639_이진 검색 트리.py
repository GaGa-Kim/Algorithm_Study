import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

tree = []
while True:
    try:
        n = int(input())
        tree.append(n)
    except:
        break

# 이진 탐색 (검색) 트리
def post_order(start, end):
    if start > end:
        return
    # 왼쪽 서브 트리와 오른쪽 서브 트리를 나누는 mid
    mid = end + 1 # 오른쪽 서브 트리가 없다고 가정하고 초기 mid를 설정
    # 반복문이 반복될 때마다 mid가 바뀜
    for i in range(start + 1, end + 1):
        # 루트보다 클 경우 
        if tree[start] < tree[i]:
            # 오른쪽 서브 트리의 시작 노드를 mid로 설정
            mid = i
            break
    post_order(start + 1, mid - 1) # 왼쪽 서브트리 확인
    post_order(mid, end) # 오른쪽 서브트리 확인
    print(tree[start])

post_order(0, len(tree) - 1)