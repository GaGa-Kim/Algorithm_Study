n, k = map(int, input().split())
numbers = list(map(int, input().split()))

count = 0 # 원소 삭제 횟수
tmp = 0 # 현재 짝수로 이루어져 있는 연속한 부분 수열 길이
answer = 0
end = 0 # 끝점

# 시작점을 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while (count <= k and end < n):
        # 원소가 홀수일 경우
        if numbers[end] % 2 == 1:
            # 삭제
            count += 1
        # 원소가 짝수일 경우
        else:
            # 부분 수열 길이 증가
            tmp += 1
        end += 1

        # 만약 시작점부터 끝점이 될 때까지 원소 삭제 횟수가 k번을 넘지 않는다면 최대 짝수 부분 수열 길이가 되므로 바로 바로 출력 후 종료
        if start == 0 and end == n:
            answer = tmp
            break

    # k + 1번째 삭제일 때 while문을 빠져나오므로
    if count == k + 1:
        # 부분 수열 길이 갱신
        answer = max(tmp, answer)

    # 시작점이 홀수라면
    if numbers[start] % 2 == 1:
        # 시작점을 옮기기 전에 원소 삭제 횟수 감소
        count -= 1
    # 시작점이 짝수라면
    else:
        # 시작점을 옮기기 전에 부분 수열 길이 감소
        tmp -= 1
print(answer)
