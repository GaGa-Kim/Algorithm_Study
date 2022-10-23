import sys
input = sys.stdin.readline

# 입력되는 나무 종 딕셔너리
trees = {}
# 입력되는 총 나무 수
count = 0
while True:
    name = input().rstrip()
    # 입력이 없으면 종료
    if not name:
        break
    count += 1
    # 이미 나무 종이 딕셔너리에 등록되었다면 
    if name in trees:
        trees[name] += 1
    # 새로운 나무 종이라면
    else:
        trees[name] = 1

# 나무 종의 이름을 사전순으로 정렬 
trees = sorted(trees.items())
for tree in trees:
    print("%s %.4f" %(tree[0], tree[1] / count * 100))