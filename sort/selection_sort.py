from random import shuffle


def selection_sort(nums):
    nl = len(nums)
    for i in range(nl - 1):
        mini = None
        for j in range(i, nl):
            if mini == None or nums[j] <= mini:
                mini, ind = nums[j], j
        nums[i], nums[ind] = nums[ind], nums[i]
    return nums


if __name__ == '__main__':
    nums = range(10)
    shuffle(nums)
    print(nums)
    sorted_nums = selection_sort(nums)
    print(sorted_nums)
