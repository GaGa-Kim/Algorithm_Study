# 프로그래머스 42889번

# 실패율) 스테이지 도달o, 클리어는 x 플레이어 수 / 스테이지 도달o 플레이어 수
# 전체 스테이지 개수 ~ N, 
# 사용자가 현재 멈춰있는 스테이지 번호 담긴 배열 ~ stages

# 만약 실패율 같은 스테이지 있으면 작은 번호가 먼저 옴
# 스테이지에 도달한 유저 x ~ 실패율 0으로 정의

def solution(N, stages):
    answer = []
    length = len(stages)
    
    # 스테이지 번호 1 ~ N
    for i in range(1, N+1):
        # 해당 스테이지에 멈춰 있는 플레이어 수 계산
        count = stages.count(i)
        
        # 실패율 계산
        if length == 0:
            fail = 0
        else:
            fail = count / length
            
        # 리스트에 (스테이지 번호, 실패율) 원소 삽입
        answer.append((i, fail))
        length -= count
        
    # 실패율을 기준으로 각 스테이지 내림차순 정렬
    answer = sorted(answer, key = lambda t: t[1], reverse=True)
    
    # 정렬된 스테이지 번호 출력
    answer = [i[0] for i in answer]
    return answer