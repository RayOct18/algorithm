import heapq


def greedy(lists, sizes):
    heapq.heapify(sizes)
    total = 0
    while len(sizes) > 1:
        node = 0
        node = heapq.heappop(sizes) + heapq.heappop(sizes)
        heapq.heappush(sizes, node)
        total += node
    return total


if __name__ == '__main__':
    sizes = [20, 30, 10, 5, 30]
    lists = list(range(len(sizes)))
    print(greedy(lists, sizes))