# 완전 탐색 유형

# 문자열에서 같은 값이 연속해서 나타나는 것을 
# 그 문자의 개수와 반복되는 값으로 표현하여 문자열 압축
# ex) aabbaccc => 2a2ba3c

# 문자열 s가 매개변수로 주어질 때, 
# 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이 return

# 1 <= s의 길이 <= 1,000
# s는 알파벳 소문자로만 구성

def solution(s):
    answer = len(s)
    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s)//2+1):
        compressed = ""
        prev = s[0:step] # 앞에서부터 step만큼의 문자열 추출
        count = 1 # 압축 횟수
        # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 이전 상태와 동일하다면 압축 횟수 증가
            if prev == s[j:j+step]:
                count += 1
            # 더 이상 압축하지 못하는 경우
            else:
                compressed += str(count) + prev if count>=2 else prev
                # 상태 초기화
                prev = s[j: j+step]
                count = 1
        # 남아 있는 문자열 처리
        compressed += str(count) + prev if count>=2 else prev
        answer = min(answer, len(compressed))   
    return answer


# (!) 입력으로 주어지는 문자열의 길이가 1,000이하이므로 완전 탐색 수행 가능
# 길이가 N인 문자열이 주어지면 1 ~ N/2의 모든 수를 단위로 하여 
# 문자열 압축하는 방법 모두 확인, 가장 짧게 압축되는 길이 출력