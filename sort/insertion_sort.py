from random import shuffle
from sorted_plot import plot_bar


def insertion_sort(nums):
    nl = len(nums)
    for i in range(1, nl):
        key = nums[i]
        for j in reversed(range(i)):
            if nums[j] < key:
                j += 1
                break
        plot_bar(nums, i)
        insert_num = nums.pop(i)
        nums.insert(j, insert_num)
        plot_bar(nums, j)
    return nums


if __name__ == '__main__':
    nums = list(range(20))
    shuffle(nums)
    sorted_nums = insertion_sort(nums)
    print(sorted_nums)
