import sys
input = sys.stdin.readline

n, c = map(int, input().split())
m = int(input())
boxes = []
for _ in range(m):
    start, end, amount = map(int, input().split())
    boxes.append([start, end, amount])
# [받는 마을, 보내는 마을] 순으로 정렬
boxes.sort(key= lambda x: (x[1], x[0]))

# 마을 당 수용가능한 박스 개수
capacity = [c] * (n + 1)
answer = 0
for start, end, amount in boxes:
    # 보내는 마을부터 받는 마을까지 얼만큼 박스를 옮길 수 있는지
    maxBox = amount
    for i in range(start, end):
        maxBox = min(maxBox, capacity[i])
    for j in range(start, end):
        capacity[j] -= maxBox
    answer += maxBox
print(answer)