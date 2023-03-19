import sys
input = sys.stdin.readline

n = int(input())
weights = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

weights.sort(reverse=True)
boxes.sort(reverse=True)

time = 0
# 가장 큰 무게 제한보다 박스의 무게가 크다면 옮길 수 없음
if boxes[0] > weights[0]:
    print(-1)
else:
    while len(boxes) > 0:
        for weight in weights:
            for box in boxes:
                # 박스를 실을 수 있다면 
                if weight >= box:
                    boxes.remove(box)
                    break
        time += 1
    print(time)
