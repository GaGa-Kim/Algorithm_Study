# 프로그래머스 - 2020 카카오 블라인드 채용
# 2차원 배열 key와 lock이 매개변수로 주어질 때,
# 열쇠로 자물쇠를 열 수 있으면 true, 아니면 fale 리턴하는 함수 작성

# 2차원 리스트 90도 회전
def rotate_a_matrix_by_90_degree(a):
    n = len(a)      # 행 길이 계산
    m = len(a[0])   # 열 길이 계산
    result = [[0] * n for _ in range(m)] # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

# 자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j] != 1:
                return False
    return True
    

def solution(key, lock):
    n = len(lock)
    m = len(key)
    
    # 자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0] * (n+3) for _ in range(n*3)]
    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
            
    # 4가지 방향에 대해 확인
    for _ in range(4):
        key = rotate_a_matrix_by_90_degree(key) # 열쇠 회전
        # 자물쇠를 3배 늘려놓은 상태이므로 0 ~ 2배까지를 시작점으로 함
        for x in range(n*2):
            for y in range(n*2):
                # 자물쇠에 열쇠 끼워 넣기
                # 원래 자물쇠 시작점에서 열쇠만큼 움직이면서 각각 원소 더함
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+i] += key[i][j]
                
                # 새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사
                if check(new_lock) == True:
                    return True
                # 자물쇠에서 열쇠 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+i] -= key[i][j]
    return False