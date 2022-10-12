n = int(input())
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))

white_count = 0
blue_count = 0
def make_color_paper(n, paper):
    global white_count
    global blue_count
    check_count = 0
    for i in range(n):
        check_count += sum(paper[i])
    # 모두 0이라면 하얀색 색종이
    if check_count == 0:
        white_count += 1
    # 모두 1이라면 파란색 색종이
    elif check_count == n * n:
        blue_count += 1
    # 색종이가 만들어지지 않을 경우, 네 개의 색종이로 나누어 반복
    else:
        paper_temp = [paper[i][0 : n//2] for i in range(0, n//2)]
        make_color_paper(n//2, paper_temp) 
        paper_temp = [paper[i][0 : n//2] for i in range(n//2, n)]
        make_color_paper(n//2, paper_temp)
        paper_temp = [paper[i][n//2 : n] for i in range(0, n//2)]
        make_color_paper(n//2, paper_temp)
        paper_temp = [paper[i][n//2 : n] for i in range(n//2, n)]
        make_color_paper(n//2, paper_temp)

make_color_paper(n, paper)
print(white_count)
print(blue_count)