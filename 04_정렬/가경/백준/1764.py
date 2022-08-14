import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array1 = [input().rstrip() for _ in range(n)]
array2 = [input().rstrip() for _ in range(m)]

# array1과 array2의 교집합을 리스트로 만들고 사전순 정렬
result = sorted(list(set(array1) & set(array2)))
print(len(result))
for i in result:
    print(i)
