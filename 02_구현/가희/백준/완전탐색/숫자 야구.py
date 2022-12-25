# 2503번
# 영수가 생각하고 있을 가능성이 있는 답의 총 개수를 출력하는 프로그램

# 스트라이크 ~ 동일한 자리 수
# 볼 ~ 동일한 수
# 몇 스트라이크 몇 볼인지 답해주고, 3 스트라이크가 되면 게임 종료

# ***
# 1. 완전 탐색) 서로 다른 수로 구성된 세 자리수의 전체 순열을 미리 구해놓음
# 2. 전체 순열, 입력받은 숫자를 비교하여 조건(s, b)과 다르면 배열에서 제거
# 3. 최종적으로 배열의 길이가 답이 됨
# ***

# 중복되지 않는 수들의 배열(순열)을 구하기 위함
from itertools import permutations
num = list(permutations(('1', '2', '3', '4', '5', '6', '7', '8', '9'), 3))


# 질문 수 1 <= n <= 100
n = int(input())

for _ in range(n):
    q, s, b = map(int, input().split())
    q = list(str(q))
    
    removeCnt = 0
    for i in range(len(num)):
        strike = ball = 0
        i -= removeCnt # num[0]부터 조회
        
        for j in range(3):
            # 질문한 숫자와 num의 숫자가 같고, 동일한 자리면 스트라이크
            if num[i][j] == q[j]:
                strike += 1
            # 질문한 숫자가 num의 숫자 중 하나면 볼
            elif q[j] in num[i]:
                ball += 1
                
        # 입력받은 s, b와 다르면 num에서 삭제
        if (strike != s) or (ball != b):
            num.remove(num[i])
            removeCnt += 1
                
print(len(num))   
    