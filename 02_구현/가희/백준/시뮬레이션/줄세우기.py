# 10431번
# 아이들의 키가 주어지고, 어떤 순서로 아이들이 줄서기를 할지 주어질 때,
# 아래 방법을 마지막 학생까지 시행했을 때 학생들은 총 몇 번 뒤로 물러서는지 구함

# 아무나 한 명을 뽑아 맨 앞에 세우고 다음 학생부터는 다음 과정 거침
# 1. 자기 앞에 자기보다 키 큰 학생이 없으면 그 자리에 서고 차례 끝
# 2. 자기 앞에 자기보다 키 큰 학생이 한 명 이상 있으면 그중 가장 앞에 있는
#   학생(A)의 바로 앞에 선다. 이때, A부터 그 뒤 학생들은 한 발씩 뒤로 감

# => 0 ~ i-1번째 사람들 중 i번째 사람보다 키가 큰 사람들 중 
#    제일 작은 사람의 위치 찾아야 함

# 테스트 케이스 수 1 <= p <= 1,000
p = int(input())

for _ in range(p):
    data = list(map(int, input().split()))
    t, num = data[0], data[1:]
    
    cnt = 0
    for i in range(1, len(num)):
        max_height, index = max(num)+1, i
        for j in range(i):
            if num[j] > num[i] and num[j] < max_height:
                max_height = num[j]
                index = j
        if index != i:
            num = num[:index] + [num[i]] + num[index:i] + num[i+1:]
            cnt += i - index
    print(t, cnt)