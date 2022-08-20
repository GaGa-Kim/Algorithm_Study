# n개의 원소로 구성된 두 개의 배열 A, B가 있을 때 
# 최대 k번의 바꿔치기 연산을 하여 만들 수 있는 
# 배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램

# 배열 A의 가장 작은 원소와 배열 B의 가장 큰 원소 교체
# (단, 배열 A의 원소가 배열 B의 원소보다 작을 때만)
# ~> A는 오름차순, B는 내림차순으로 정렬할 것

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else: # A의 원소가 B의 원소보다 크거나 같으면 반복 종료
        break

print(sum(a))