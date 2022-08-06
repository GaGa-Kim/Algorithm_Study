import sys
input = sys.stdin.readline

eng = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine', '0':'zero'}
m, n = map(int, input().split())
array = []
for i in range(m, n + 1):
    s = ''
    # 정수를 하나씩 확인하며 숫자 단위로 영어로 바꿈 
    for j in str(i):
        s += ''.join([eng[j]])
    array.append([i, s])
# 사전순으로 정렬
array.sort(key = lambda x: x[1])
for i in range(len(array)):
    # 10개씩 정수를 출력
    if i % 10 == 0 and i != 0:
        print()
    print(array[i][0], end=' ')