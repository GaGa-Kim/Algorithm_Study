from bisect import bisect_left

n = int(input())
array1 = list(map(int, input().split()))
array1.sort()

m = int(input())
array2 = list(map(int, input().split()))

for card in array2:
    i = bisect_left(array1, card)
    if (len(array1) > 0 and len(array1) > i and card == array1[i]):
        print(1, end =' ')
    else:
        print(0, end =' ')
