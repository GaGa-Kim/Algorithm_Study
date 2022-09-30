import sys
input = sys.stdin.readline

# 전위 순회
def pre_order(data):
    print(data, end='') 
    if tree[data][0] != '.':
        pre_order(tree[data][0]) 
    if tree[data][1] != '.':
        pre_order(tree[data][1]) 

# 중위 순회
def in_order(data):
    if tree[data][0] != '.': 
        in_order(tree[data][0]) 
    print(data, end='') 
    if tree[data][1] != '.':
        in_order(tree[data][1]) 

# 후위 순회
def post_order(data):
    if tree[data][0] != '.':
        post_order(tree[data][0]) 
    if tree[data][1] != '.':
        post_order(tree[data][1]) 
    print(data, end='') 

n = int(input())
tree = {}
for _ in range(n):
    data, left_node, right_node = input().split()
    tree[data] = [left_node, right_node]

pre_order('A') # 전위 순회
print()
in_order('A') # 중위 순회
print()
post_order('A') # 후위 순회​