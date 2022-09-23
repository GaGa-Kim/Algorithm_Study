# 11728번
# 정렬되어 있는 두 배열 A와 B가 주어질 때, 두 배열을 합친 다음 정렬해서 출력하는 프로그램

# 투 포인터 활용

# 배열 A의 크기 N, 배열 B의 크기 M
# (1 <= N,M <= 1,000,000)
n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = [0] * (n + m)  # 결과 리스트 (A 길이 + B 길이)
i = 0                   # A 인덱스
j = 0                   # B 인덱스
k = 0                   # result 인덱스

# 모든 원소가 결과 리스트에 담길 때까지 반복
while i < n or j < m:
    # B의 원소가 모두 처리되었거나, A의 원소가 더 작을 때
    if j >= m or (i < n and a[i] <= b[j]):
        # A의 원소를 결과 리스트로 옮기기
        result[k] = a[i]
        i += 1
    else: # A의 모든 원소가 처리되었거나, B의 원소가 더 작을 때
        # B의 원소를 결과 리스트로 옮기기
        result[k] = b[j]
        j += 1
    k += 1

# 결과 리스트 출력
for i in result:
    print(i, end=' ')