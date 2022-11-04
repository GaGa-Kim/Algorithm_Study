import sys
input = sys.stdin.readline

# Node를 class로 만들기
class Node:
    def __init__(self, data):
        self.data = data # 자신의 데이터
        self.child = None # 자식 노드
        self.parent = None # 부모 노드

# 자료구조를 만들어 트리 자료구조인지 아닌지 판별
def checkTree():

    # 루트 노드로부터 모든 노드로 갈 수 있는지 판별
    def checkCycle(rootNode):
        cnt = len(rootNode.child)
        for i in rootNode.child:
            cnt += checkCycle(node_dict[i])
        return cnt

    isInput = True # 테스트 케이스 입력이 계속 들어오는지 여부
    answer = True # 트리인지 아닌지 여부
    node_dict = dict() # 노드 딕셔너리
    root = None # 루트 노드
    global isWorking # 모든 테스트 케이스 종료 여부

    # 입력을 통해 자료구조 만들기
    while isInput:
        # 정수쌍 u, v로 입력을 받음
        # ['6 8', '5 3', '5 2', '6 4']
        nodes = input().rstrip().split("  ")

        # 노드가 공배열이면 트리이므로 continue로 빠져나옴
        if nodes[0] == '':
            continue
        
        # '6 8'
        for node in nodes:
            # u = 6, v = 8
            # 노드 u에서 노드 v로 가는 간선이므로 노드 v는 노드 u의 자식
            u, v = map(int, node.split(" "))
            # u, v가 둘 다 0이라면 테스트 케이스 입력의 끝
            if u == 0 and v == 0:
                # 입력 종료
                isInput = False
                break
            # u, v가 둘 다 음의 정수라면 모든 테스트 케이스의 끝
            elif u < 0 and v < 0:
                # 입력 종료
                isInput = False
                # 모든 테스트 케이스 종료
                isWorking = False
                break

            # 노드 u를 노드 딕셔너리에 저장
            if u in node_dict:
                # 이미 노드 u가 딕셔너리에 있는 노드라면 자식 노드로 v 추가
                node_dict[u].child.append(v)
            else:
                # 노드 u가 딕셔너리에 없다면 노드 딕셔너리에 추가
                node_dict[u] = Node(u)
                # 노드 u의 자식 노드로 v 추가
                node_dict[u].child = [v]

            # 노드 v를 노드 딕셔너리에 저장
            if v in node_dict:
                # 이미 노드 v가 딕셔너리에 있는 노드이며 부모가 없다면 부모 노드로 u 추가
                if node_dict[v].parent == None:
                    node_dict[v].parent = u
                else:
                    # 부모 노드가 이미 있어 부모가 2개의 노드가 될 경우 트리가 아님
                    # 즉 모든 노드는 단 하나의 들어오는 간선이 존재
                    answer = False
            else:
                # 노드 v가 딕셔너리에 없다면 노드 딕셔너리에 추가
                node_dict[v] = Node(v)
                # 노드 v의 무도 노드로 u 추가
                node_dict[v].parent = u
                # 노드 v의 자식 노드로 빈 노드 추가
                node_dict[v].child = []

    # 자료구조가 트리 자료구조인지 판단

    # 공배열일 경우 트리
    if len(node_dict) == 0:
        return True

    # 부모 노드가 2개가 되는 노드가 있다면 트리가 아님
    if answer == False:
        return answer

    # 루트 노드 찾기
    for i in node_dict.values():
        # 부모가 없는 노드이면서
        if i.parent == None:
            # 루트가 존재하지 않을 경우
            if root == None:
                # 그 노드가 루트 노드
                root = i.data
            # 이미 루트가 존재할 경우
            else:
                # 부모가 없는 노드가 2개이므로 트리가 아님
                answer = False
                return answer

    # 루트 노드가 없으면 트리가 아님
    if root == None:
        return False
    
    # 루트 노드로부터 모든 노드로 갈 수 있다면 트리
    cycle = 1 + len(node_dict[root].child)
    for i in node_dict[root].child:
        cycle += checkCycle(node_dict[i])
    if cycle != len(node_dict):
        return False
    return answer

isWorking = True
number = 1
while isWorking:
    check = checkTree()
    if not isWorking:
        break
    if check:
        string = "Case " + str(number) + " is a tree."
        print(string)
    else:
        string = "Case " + str(number) + " is not a tree."
        print(string)
    number += 1 
