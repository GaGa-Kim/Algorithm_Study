# 2020 카카오 신입 공채 1차

# "균형잡힌 괄호 문자열"의 인덱스 반환
def balanced_index(p):
    count = 0 # 왼쪽 괄호 개수
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0: # () 개수가 같으면 균형잡힌 괄호 문자열
            return i

# "올바른 괄호 문자열"인지 판단
def check_proper(p):
    count = 0 # 왼쪽 괄호 개수
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0: # 쌍이 맞지 않는 경우
                return False
            count -= 1
    return True # 쌍이 맞는 경우

    
def solution(p):
    answer = ''
    
    # 1. 입력이 빈 문자열인 경우, 빈 문자열 반환
    if p == '':
        return answer
    
    # 2. 문자열 p를 "균형잡힌 괄호 문자열" u, v로 분리
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:] 
    
    # 3. 문자열 u가 "올바른 괄호 문자열"이면
    if check_proper(u):
        # 문자열 v에 대해 1단계부터 다시 수행한 뒤,
        # 수행 결과 문자열을 u에 이어 붙인 후 반환
        answer = u + solution(v)
    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면
    else:
        # 4-1. 빈 문자열에 첫 번째 문자로 '(' 붙임
        answer = '('
        # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행하고, 
        #수행 결과 문자열을 이어 붙임
        answer += solution(v)
        # 4-3. ')' 다시 붙임
        answer += ')'
        # 4-4. u의 첫 번째, 마지막 문자 제거 후
        # 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙임
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u) # '구분자'.join(리스트)
    # 생성된 문자열 반환
    return answer