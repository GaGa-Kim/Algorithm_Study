n = input()
m = input()

count = 0
index = 0
for i in range(len(n)):
    # 이미 단어를 센 곳이므로 건너뜀
    if index > i:
        continue
    # 찾는 단어와 동일할 때 개수 증가
    if m == n[i : i + len(m)]:
        count += 1
        # 중복되지 않도록 인덱스 위치 변경
        index = i + len(m)

print(count)