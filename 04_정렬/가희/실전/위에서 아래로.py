# 수열을 내림차순으로 정렬하는 프로그램

# 수열에 속해있는 수 n (1 <= n <= 500)
n = int(input())

array = [int(input()) for _ in range(n)]

array = sorted(array, reverse=True)

for i in array:
    print(i, end=' ')
    
# print(*array)