# 10973번
# 1부터 N까지의 수로 이루어진 순열이 있을 때,
# 사전순으로 바로 이전에 오는 순열을 구하는 프로그램

# 사전순으로 가장 앞서는 순열은 오름차순으로 이루어진 순열,
# 가장 마지막에 오는 순열은 내림차순으로 이루어진 순열

# n (1 <= n <= 10,000)
n = int(input())
arr = list(map(int, input().split()))

# 배열을 뒤에서 부터 탐색하면서 
for i in range(n-1, 0, -1):
    # 앞자리 수가 더 큰 경우 있는지 확인
    if arr[i-1] > arr[i]:
        # 앞자리 수가 더 큰 부분을 경계로 
        for j in range(n-1, 0, -1):
            # 뒷부분 숫자 중 앞의 경계값보다 작은 값 탐색
            if arr[i-1] > arr[j]:
                # 경계값과 작은 값 자리 바꾸고
                arr[i-1], arr[j] = arr[j], arr[i-1]
                # 경계값 뒷부분 내림차순 정렬
                arr = arr[:i] + sorted(arr[i:], reverse=True)
                print(*arr) # 한 번에 출력
                exit()
                
# 사전순으로 가장 처음에 오는 순열인 경우 -1을 출력한다.
print(-1)
                


# ---------------메모리 초과-------------------
from itertools import permutations 

# n (1 <= n <= 10,000)
n = int(input())

input_permutation = list(map(int, input().split()))

num_list = [i for i in range(1, n+1)]
perm_list = list(permutations(num_list))

for i in range(len(perm_list)):
    if list(perm_list[i]) == input_permutation:
        # 만약 사전순으로 가장 처음에 오는 순열인 경우 -1 출력
        if i == 0:
            print(-1)
        else:
            for j in perm_list[i-1]:
                print(j, end=' ')
