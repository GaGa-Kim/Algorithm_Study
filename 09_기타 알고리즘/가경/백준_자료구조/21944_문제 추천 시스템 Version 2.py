from collections import defaultdict
import sys
input = sys.stdin.readline

rank_prob = 100001
n = int(input())
# recommend G x : 우선순위 G > L > P
recommend1_dic = defaultdict(dict) 
# recommend2 x : 우선순위 L > P
recommend2_dic = defaultdict(dict)
# recommend3 x L : 우선순위 L > P > -1
recommend3_dic = defaultdict(dict)  
# 전체 문제
problem_dict = dict()

for _ in range(n):
    P, L, G = map(int, input().split())
    calc_num = L * rank_prob + P # 난이도와 문제 번호 합치기 (난이도 * 100001 +  문제 번호)
    recommend1_dic[G][calc_num] = 1 # {G:{LP:bool}}
    recommend2_dic[calc_num] = 1 # {LP:bool}
    recommend3_dic[L][P] = 1 # {L:{P:bool}}
    problem_dict[P] = [L, G] # {P:[L, G]}

m = int(input())
for _ in range(m):
    command, *arg = input().split()
    # recommend G x
    if command == 'recommend':
        G, x = map(int, arg)
        # x가 양수인 경우
        if x > 0:
            # G인 문제 중 가장 어려운 문제 (G에 해당하는 값중 -> L이 높고 -> P가 높은 것)
            calc_num = max(recommend1_dic[G].keys())
        # x가 음수인 경우
        else:
            # G인 문제 중 가장 쉬운 문제 (G에 해당하는 값중 -> L이 낮고 -> P가 낮은 것)
            calc_num = min(recommend1_dic[G].keys())
        # 난이도와 문제 번호 합친 것에서 난이도와 문제 번호 따로 구해주기
        L = calc_num // rank_prob
        P = calc_num % rank_prob
        # 문제 번호 출력
        print(P)
    # recommend2 x
    elif command == 'recommend2':
        x = int(arg[0])
        # x가 양수인 경우
        if x > 0:
            # 가장 어려운 문제 (L이 크고 -> P가 큰 것)
            calc_num = max(recommend2_dic.keys())  
        # x가 음수인 경우
        else:
            # 가장 쉬운 문제 (L이 낮고 -> P가 낮은 것)
            calc_num = min(recommend2_dic.keys())
        # 난이도와 문제 번호 합친 것에서 난이도와 문제 번호 따로 구해주기
        L = calc_num // rank_prob
        P = calc_num % rank_prob
        # 문제 번호 출력
        print(P)
    # recommend3 x L
    elif command == 'recommend3':
        x, target_L = map(int, arg)
        # x가 음수인 경우 (x가 양수인 경우에는 크거나 같은 문제이므로 빼지 않음)
        if x < 0:
            # x가 음수인 경우 난이도 타겟 L보다 작아야 함
            target_L = target_L + x   
        result = -1 # 초기값 설정 (조건을 충족하는 문제가 없을 경우)
        while 0 <= target_L <= 100:
            # 타켓 L 찾기
            if recommend3_dic.get(target_L):
                # x가 양수인 경우
                if x > 0:
                    # 난이도 타켓 L보다 크거나 같은 문제 중 가장 쉬운 문제 (타겟 L보다 L이 같거나 크고 -> L이 작고 -> P가 낮은 것)
                    result = min(recommend3_dic[target_L].keys())
                # x가 음수인 경우
                else:
                    # 난이도 타켓 L보다 작은 문제 중 가장 어려운 문제 (타겟 L보다 L이 작고 -> L이 크고 -> P가 높은 것)
                    result = max(recommend3_dic[target_L].keys())
                break
            # x가 양수인 경우 1을 더하고, x가 음수인 경우 1을 줄임
            target_L = target_L + x
        # 문제 번호 출력
        print(result)
    # solved P
    elif command == 'solved':
        P = int(arg[0])
        # 문제 번호 P의 난이도 L과 알고리즘 분류 G를 구함
        L, G = problem_dict[P]
        # 난이도와 문제 번호 합친 것을 구함
        calc_num = L * rank_prob + P
        # 각 dic에서 값 제거
        del recommend3_dic[L][P]      
        del recommend2_dic[calc_num]
        del recommend1_dic[G][calc_num]
    # add P L g
    else:
        P, L, G = map(int, arg)
        calc_num = L * rank_prob + P
        recommend1_dic[G][calc_num] = 1
        recommend2_dic[calc_num] = 1
        recommend3_dic[L][P] = 1
        problem_dict[P] = [L, G]