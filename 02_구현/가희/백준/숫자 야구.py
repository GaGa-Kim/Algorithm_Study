# 2503번
# 영수가 생각하고 있을 가능성이 있는 답의 총 개수 출력하는 프로그램

# 스트라이크 ~ 동일한 자리 동일한 수
# 볼 ~ 동일한 수
# 3 스트라이크 되면 게임 종료, 
# 아니라면 새로운 수 생각해 다시 물음

# 중복되지 않는 수들의 배열(순열)을 구하기 위해 사용
from itertools import permutations 
# 서로 다른 수의 세 자리 숫자
num = list(permutations(('1', '2', '3', '4', '5', '6', '7', '8', '9'), 3))

# 민혁이가 영수에게 질문한 횟수 (1 <= n <= 100)
n = int(input())

# 민혁이가 질문한 세 자리수(q),
# 스트라이크 개수(s),
# 볼의 개수 나타내는 정수(b)
for _ in range(n):
    q, s, b = map(int, input().split())
    q = list(str(q))
    
    removeCnt = 0
    for i in range(len(num)):
        strike = ball = 0
        i -= removeCnt # num[0]부터 조회
        
        for j in range(3):
            # 질문한 숫자와 num의 숫자가 같고 동일한 자리면 스트라이크
            if num[i][j] == q[j]:
                strike += 1
            # 질문한 숫자가 num의의 숫자 중 하나면 볼
            elif q[j] in num[i]:
                ball += 1
        # 입력받은 s, b와 다르면 num에서 삭제
        if (strike != s) or (ball != b):
            num.remove(num[i])
            removeCnt += 1

print(len(num))

# 전체 순열을 입력받은 숫자와 비교해 조건(s, b)과 다르면 배열에서 제거
# 최종적으로 배열의 길이가 답이 됨
