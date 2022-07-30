# 1966번
# 각 테스트 케이스에 대해 문서가 몇 번째로 인쇄되는지 출력

# <인쇄 조건>
# 1. 현재 큐의 가장 앞에 있는 문서의 중요도 확인
# 2. 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있으면,
#   이 문서를 인쇄하지 않고 큐의 가장 뒤에 재배치. 그렇지 않으면 바로 인쇄
# ex) ABCD 각 중요도 2143 ~> C > D > A > B 순 인쇄

# 테스트 케이스 수
testcase = int(input())

for _ in range(testcase):
    # 문서의 개수 (1 ≤ N ≤ 100), 
    # 현재 큐에서 확인하려는 문서의 위치(0 ≤ M < N )
    n, m = map(int, input().split())

    # n개의 문서의 중요도
    priority = list(map(int, input().split()))
    
    # 확인하려는 문서 위치 따로 저장
    check = [0 for _ in range(n)]
    check[m] = 1
    
    cnt = 0
    while priority:
        # 0 ~ 선입선출 ~> 맨 앞부터 확인
        # 맨 앞 문서가 중요도 제일 높으면 인쇄 
        if priority[0] == max(priority):
            cnt += 1
            if check[0] == 1:
                print(cnt)
                break
            priority.pop(0)
            check.pop(0)
        else:
            priority.append(priority.pop(0))
            check.append(check.pop(0))