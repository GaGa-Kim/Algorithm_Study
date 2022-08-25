import sys
input = sys.stdin.readline

a, b = map(int, input().split())
array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))

# array1과 array2의 차집합을 리스트로 만들고 사전순 정렬
result = sorted(list(set(array1) - set(array2)))
print(len(result))
for i in result:
    print(i, end=" ")
