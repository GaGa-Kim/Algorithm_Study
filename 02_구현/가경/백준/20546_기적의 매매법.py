import sys
input = sys.stdin.readline

n = int(input())
stocks = list(map(int, input().split()))

def bnp(money):
    result = 0
    for stock in stocks:
        if stock <= money:
            result += money // stock
            money -= (money // stock) * stock
    return stocks[13] * result + money

def timing(money):
    result = 0
    down_count = 0
    up_count = 0
    for i in range(1, len(stocks)):
        # 매수
        if stocks[i - 1] > stocks[i]:
            down_count += 1
            up_count = 0
            if down_count >= 3:
                result += money // stocks[i]
                money -= (money // stocks[i]) * stocks[i]
        # 매도
        if stocks[i - 1] < stocks[i]:
            up_count += 1
            down_count = 0
            if up_count >= 3:
                money += result * stocks[i]
                result = 0
        if stocks[i - 1] == stocks[i]:
            down_count = 0
            up_count = 0
    return stocks[13] * result + money

if bnp(n) > timing(n):
    print('BNP')
elif bnp(n) < timing(n):
    print('TIMING')
else:
    print('SAMESAME')