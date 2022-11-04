import sys
input = sys.stdin.readline

# Node를 class로 만들기
class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data # 자신의 데이터
        self.left_node = left_node # 왼쪽 노드
        self.right_node = right_node # 오른쪽 노드

# 전위 순회
def pre_order(node):
    print(node.data, end='')
    if node.left_node != '.':
        pre_order(tree[node.left_node]) 
    if node.right_node != '.':
        pre_order(tree[node.right_node]) 

# 중위 순회
def in_order(node):
    if node.left_node != '.':
        in_order(tree[node.left_node]) 
    print(node.data, end='')
    if node.right_node != '.':
        in_order(tree[node.right_node]) 

# 후위 순회
def post_order(node):
    if node.left_node != '.':
        post_order(tree[node.left_node]) 
    if node.right_node != '.':
        post_order(tree[node.right_node]) 
    print(node.data, end='') 

n = int(input())
tree = {}
for _ in range(n):
    data, left_node, right_node = input().split()
    tree[data] = Node(data, left_node, right_node)

pre_order(tree['A']) # 전위 순회
print()
in_order(tree['A']) # 중위 순회
print()
post_order(tree['A']) # 후위 순회​