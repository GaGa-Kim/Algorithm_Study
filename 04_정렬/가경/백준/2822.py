points = []
for i in range(8):
    points.append((i + 1, int(input())))
points = sorted(points, key = lambda x : -x[1])

sum = 0 # 참가자의 총점
answer = [] # 어떤 문제가 최종 점수에 포함되는지
for j in range(0, 5):
    sum += points[j][1]
    answer.append(points[j][0]) 

answer.sort()
print(sum)
for i in answer:
    print(i, end=' ')
