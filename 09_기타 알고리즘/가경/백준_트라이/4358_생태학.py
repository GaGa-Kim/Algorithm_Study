import sys
input = sys.stdin.readline

# Node를 class로 만들기
class Node(object):
    def __init__(self, key, data=None):
        self.key = key # 해당 노드의 문자
        self.data = data # 문자열이 끝날 경우의 문자열
        self.children = {} # 해당 노드의 자식 노드

# Trie 구조
class Trie(object):
    # Head
    def __init__(self):
        self.head = Node(None)
    # 문자열 삽입 (자식 노드로 문자열 하나씩 추가)
    def insert(self, string):
        current_node = self.head
        # 삽입할 string 각각의 문자에 대해 자식 노드를 만들며 내려감
        for char in string:
            # 자식 노드 중 같은 문자가 없다면 노드 생성
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            # 같은 문자가 있다면 노드 생성 없이 해당 노드로 이동
            current_node = current_node.children[char]
        # 문자열이 끝난 지점의 노드의 data 값에 해당 문자열 입력
        current_node.data = string
    # 문자열이 존재하는지 탐색
    def search(self, string):
        current_node = self.head
        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False
        # 탐색이 끝난 후 해당 노드의 data 값이 존재한다면 문자열이 있는 것
        if current_node.data != None:
            return True

# 입력되는 나무 종 딕셔너리
trees = {}
# 입력되는 총 나무 수
count = 0
treeTrie = Trie()
while True:
    name = input().rstrip()
    # 입력이 없으면 종료
    if not name:
        break
    count += 1
    # 이미 나무 종이 딕셔너리에 등록되었다면 
    if treeTrie.search(name):
        trees[name] += 1
    # 새로운 나무 종이라면
    else:
        treeTrie.insert(name)
        trees[name] = 1

# 나무 종의 이름을 사전순으로 정렬 
trees = sorted(trees.items())
for tree in trees:
    print("%s %.4f" %(tree[0], tree[1] / count * 100))