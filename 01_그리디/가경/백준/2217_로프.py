n = int(input())
weight = []
for _ in range(n):
    weight.append(int(input()))

weight.sort(reverse=True)

answer = []
for i in range(n):
    # 로프가 들 수 있는 중량 * 병렬 연결 로프 갯수
    answer.append(weight[i] * (i + 1))
print(max(answer))