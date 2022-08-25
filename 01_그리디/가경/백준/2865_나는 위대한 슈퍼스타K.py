import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
scores = {}
for i in range(n):
    # 1번 참가자부터
    scores[i + 1] = 0

for i in range(m):
    tmp = list(map(float, input().split()))
    # 0 부터 2 숫자만큼의 간격으로 n + 2 까지의 점수 범위를 반환
    for j in range(0, n + 2, 2):
        # 이번 장르의 점수가 이전의 점수보다 더 높다면
        if tmp[j + 1] > scores[tmp[j]]:
            scores[tmp[j]] = tmp[j + 1]
# 딕셔너리에서 점수들(values)만 가져와서 큰 순으로 정렬하고 k명 만큼만 뽑아서 합을 구함
scores = sorted(scores.values(), reverse=True)
print("%.1f" %(sum(scores[:k])))
