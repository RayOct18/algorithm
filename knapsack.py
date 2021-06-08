

def knapSack(m, profit, weights):
    n = len(profit)
    p_w = [p / w for p, w in zip(profit, weights)]
    take = [0] * n

    while m > 0:
        max_pw = [0, 0]
        for i, p in enumerate(p_w):
            if p > max_pw[0] and take[i] == 0:
                max_pw = [p, i]
        i = max_pw[1]
        m -= weights[i]
        take[i] = (weights[i] + m) / weights[i] if m < 0 else 1
    return sum([profit[i] * t for i, t in enumerate(take)])


if __name__ == '__main__':

    # m = 15
    # profit = [10, 5, 15, 7, 6, 18, 3]
    # weights = [2, 3, 5, 7, 1, 4, 1]
    m = 50
    profit = [60, 100, 120]
    weights = [10, 20, 30]

    print(knapSack(m, profit, weights))