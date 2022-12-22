# 1436번 
# n번째 영화의 제목에 들어간 숫자를 출력하는 프로그램

# 종말의 숫자: 어떤 수에 6이 적어도 3개이상 연속으로 들어가는 수
# n번째 영화 제목 ~ 세상의 종말(n번째로 작은 종말의 숫자)


# 820ms-------------------------------------------
endNum = [] 
i = 1
while True:
    if len(endNum) == 10000:
        break
    if '666' in str(i):
        endNum.append(i)
    i += 1

# 1 <= n <= 10,000
n = int(input())
print(endNum[n-1])

# 660ms-------------------------------------------
n = int(input())
endNum = 666

cnt = 0
while True:
    if '666' in str(endNum):
        cnt += 1
        
    # cnt가 구해야하는 n번째 영화라면 endNum 출력
    if cnt == n:
        print(endNum)
        break
    
    endNum += 1





