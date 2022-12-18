# 프로그래머스 - 2020 카카오 신입 공채

# 현재 설치된 구조물이 가능한 구조물인지 확인
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:          # 기둥인 경우
            # 바닥 위 혹은 보의 한쪽 끝부분 위 혹은 다른 기둥 위라면 가능
            if y==0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        if stuff == 1:          # 보인 경우
            # 한쪽 끝부분이 기둥 위 혹은 양쪽 끝부분이 다른 보와 동시에 연결
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer 
                                                                    and [x+1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame: # 작업(frame)의 개수는 최대 1,000개
        x, y, stuff, operate = frame
        if operate == 0:                     # 삭제인 경우
            answer.remove([x, y, stuff])     # 일단 삭제 해본 뒤에
            if not possible(answer):         # 가능한 구조물인지 확인
                answer.append([x, y, stuff]) # 가능한 구조물이 아니면 다시 설치
        
        if operate == 1:                     # 설치하는 경우
            answer.append([x, y, stuff])     # 일단 설치 해본 뒤에
            if not possible(answer):         # 가능한 구조물인지 확인
                answer.remove([x, y, stuff]) # 가능한 구조물이 아니면 다시 삭제             
    return sorted(answer) # 정렬된 결과 리턴