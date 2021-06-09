

def greedy(profits, deadlines):
    n = len(profits)
    cache = [-1] * max(deadlines)
    for i, d in enumerate(deadlines):
        while d > 0:
            if cache[d-1] == -1:
                cache[d-1] = i
                break
            d -= 1
    print(cache)
    return sum([profits[c] for c in cache])


if __name__ == '__main__':
    # profits = [20, 15, 10, 5, 1]
    # deadlines = [2, 2, 1, 3, 3]
    profits = [35, 30, 25, 20, 15, 12, 5]
    deadlines = [3, 4, 4, 2, 3, 1, 2]
    print(greedy(profits, deadlines))