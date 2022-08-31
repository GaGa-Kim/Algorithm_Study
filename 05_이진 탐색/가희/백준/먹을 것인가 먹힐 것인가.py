# 7795번
# A와 B의 크기가 주어졌을 때, 
# A의 크기가 B보다 큰 쌍이 몇개나 있는지 구하는 프로그램

# A는 B를 먹고, A는 자기보다 크기가 작은 먹이만 먹을 수 있다.

import sys
input = sys.stdin.readline
import bisect

# 테스트 케이스 개수 t
t = int(input())

for _ in range(t):
    # A의 수 n, B의 수 m (1 <= n, m <= 20,000)
    n, m = map(int, input().split())
    
    # A의 크기
    a_size = sorted(list(map(int, input().split())))
    # B의 크기
    b_size = sorted(list(map(int, input().split())))
    
    cnt = 0
    for i in a_size:
        # bisect(a, x) ~ a에 있는 x의 오른쪽에 오는 삽입 위치 리턴
        cnt += bisect.bisect(b_size, i-1)
    
    print(cnt)