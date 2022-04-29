# 실패율.py
def solution(N, stages): # 스테이지 개수, 사용자가 현재 도전 중인 스테이지의 번호
    answer = []
    length = len(stages)

    # 스테이지 번호를 1부터 N까지 증가시키며
    for i in range(1, N + 1):
        # 해당 스테이지에 머물러 있는 사람의 수 계산
        count = stages.count(i)

        # 실패율 계산
        # 스테이지에 도달한 유저가 없는 경우
        if length == 0:
            fail = 0
        # 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어의 수
        # 1단계는 모두 도달했으므로 사용자 수인 length로 나누어준 후, 다음 단계부터는 count만큼 감소
        else:
            fail = count / length

        # 리스트에 (스테이지 번호, 실패율) 원소 삽입
        answer.append((i, fail))
        length -= count

    # 실패율을 기준으로 각 스테이지를 실패율을 기준으로 내림차순 정렬
    answer = sorted(answer, key=lambda t:t[1], reverse=True)

    # 정렬된 스테이지 번호 출력
    answer = [i[0] for i in answer]
    return answer