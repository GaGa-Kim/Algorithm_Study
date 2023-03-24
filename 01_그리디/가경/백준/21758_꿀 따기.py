import sys
input = sys.stdin.readline

n = int(input())
honey = list(map(int, input().split()))

# 누적합
prefix_sum = []
prefix_sum.append(honey[0])
for i in range(1, n):
    prefix_sum.append(prefix_sum[i - 1] + honey[i])

answer = 0
# 벌벌통 (오른쪽 끝에 벌통, 왼쪽 끝에 벌1, i번째 위치에 벌2)
for i in range(1, n - 1):
    # 왼쪽 끝에 있는 벌1이 따는 꿀의 양 - i번째에 벌2가 있을 경우 꿀의 양 + i번째에 있는 벌2가 따는 꿀의 양
    temp = prefix_sum[n - 1] - honey[0] - honey[i] + prefix_sum[n - 1] - prefix_sum[i]
    answer = max(answer, temp)

# 통벌벌 (왼쪽 끝에 벌통, 오른쪽 끝에 벌1, i번째 위치에 벌2)
for i in range(1, n - 1):
    # 오른쪽 끝에 있는 벌1이 따는 꿀의 양 - i번째에 벌2가 있을 경우 꿀의 양 + i번째에 있는 벌2가 따는 꿀의 양
    temp = prefix_sum[n - 2] - honey[i] + prefix_sum[i - 1]
    answer = max(answer, temp)

# 벌통벌 (i번째 위치에 벌통, 왼쪽 끝에 벌1, 오른쪽 끝에 벌 2)
for i in range(1, n - 1):
    # 중복해서 딸 수 있는 꿀은 벌통 위치에 존재하는 꿀 뿐이므로
    # 좌우 원소 끝을 제외한 꿀의 양을 구한 후 꿀통의 위치인 i번째 꿀의 양을 한 번 더 더해줌
    temp = prefix_sum[n - 2] - honey[0] + honey[i]
    answer = max(answer, temp)

print(answer)