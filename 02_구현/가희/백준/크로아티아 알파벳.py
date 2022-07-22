# 2941번
# 단어가 주어졌을 때 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력

# dz, lj, nj는 무조건 하나의 알파벳으로 사용
# 목록에 없는 알파벳은 한 글자씩 셈

croatia = [ 'c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=' ]

# 0 < word <= 100, 알파벳 소문자, '-', '='로만 구성
word = input()

for i in croatia:
    # 위 목록에 있는 알파벳은 한 글자(*)로 치환
    word = word.replace(i, '*')
print(len(word))