import sys
input = sys.stdin.readline

n, m = map(int, input().split())
answer = []

def backtracking(start):
    # 길이가 m인 경우
    if len(answer) == m:
        # 수열 출력
        print(" ".join(map(str, answer)))
        return
    for i in range(start, n + 1):
        # 수열에 중복된 값이 없다면
        if i not in answer:
            answer.append(i)
            # 재귀함수 호출
            backtracking(i)
            # return으로 돌아와서 answer를 비워줌
            answer.pop()

backtracking(1)