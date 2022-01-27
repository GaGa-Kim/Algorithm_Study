# 7_트리의 순회.py
class Node: # 노드 클래스를 정의해서 자신의 데이터, 왼쪽 노드, 오른쪽 노드 명시
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

# 전위 순회
def pre_order(node):
    print(node.data, end=' ') # 자기 자신
    if node.left_node != None:
        pre_order(tree[node.left_node]) # 왼쪽
    if node.right_node != None:
        pre_order(tree[node.right_node]) # 오른쪽

# 중위 순회
def in_order(node):
    if node.left_node != None: 
        in_order(tree[node.left_node]) # 왼쪽
    print(node.data, end=' ') # 자기 자신
    if node.right_node != None:
        in_order(tree[node.right_node]) # 오른쪽

 # 후위 순회
def post_order(node):
    if node.left_node != None:
        post_order(tree[node.left_node]) # 왼쪽
    if node.right_node != None:
        post_order(tree[node.right_node]) # 오른쪽
    print(node.data, end=' ') # 자기 자신

n = int(input()) # 트리의 크기, 노드의 갯수 n
tree = {} # 딕셔너리를 통해 트리 구현

for i in range(n):
    data, left_node, right_node = input().split()
    if left_node == "None":
        left_node = None
    if  right_node == "None":
        right_node = None
    tree[data] = Node(data, left_node, right_node) # 각 노드는 자기 자신 데이터, 왼쪽 노드, 오른쪽 노드 저장

pre_order(tree['A']) # 전위 순회
print()
in_order(tree['A']) # 중위 순회
print()
post_order(tree['A']) # 후위 순회