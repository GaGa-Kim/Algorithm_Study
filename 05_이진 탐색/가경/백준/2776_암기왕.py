from bisect import bisect_left

t = int(input())
for _ in range(t):
    n = int(input())
    array1 = list(map(int, input().split()))
    array1.sort()
    
    m = int(input())
    array2 = list(map(int, input().split()))

    for i in array2:
        j = bisect_left(array1, i)
        if (len(array1) > 0 and len(array1) > j and i == array1[j]):
            print(1)
        else:
            print(0)