# 프로그래머스 - 2020 카카오 신입 공채 1차
# 원형으로 나열된 데이터를 처리하는 경우 
# ~ 길이를 2배로 늘려 원형을 일자로 만드는 작업 해주면 유리

from itertools import permutations


def solution(n, weak, dist):
    # 길이를 2배로 늘려서 원형을 일자 형태로 변형
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    
    # 투입할 친구 수의 최솟값을 찾아야 하므로 아래와 같이 초기화
    answer = len(dist) + 1 
    
    # 0부터 length-1까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        # 친구를 나열하는 모든 경우의 수 각각에 대하여 확인
        for friends in list(permutations(dist, len(dist))):
            count = 1 # 투입할 친구 수
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count-1]
            # 시작점부터 모든 취약 지점 확인
            for index in range(start, start+length):
                # 점검할 수 있는 위치 벗어나는 경우
                if position < weak[index]:
                    count += 1 # 새로운 친구 투입
                    if count > len(dist): # 더 이상 투입 불가능하면 종료
                        break
                    position = weak[index] + friends[count-1]
            answer = min(answer, count)
    
    # 친구를 모두 투입해도 전부 점검할 수 없는 경우 -1 리턴    
    if answer > len(dist):
        return -1
    return answer