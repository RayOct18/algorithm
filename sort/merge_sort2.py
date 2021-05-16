from random import shuffle
from sorted_plot import plot_bar


def merge_sort(nums):
    if len(nums) == 1:
        return 0

    n = len(nums)
    left = nums[:n//2]
    right = nums[n//2:]

    merge_sort(left)
    merge_sort(right)

    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            nums[k] = right[j]
            j += 1
        else:
            nums[k] = left[i]
            i += 1
        k += 1

    while i < len(left):
        nums[k] = left[i]
        k += 1
        i += 1

    while j < len(right):
        nums[k] = right[j]
        k += 1
        j += 1

    plot_bar(nums, 0)

    return nums


if __name__ == '__main__':
    nums = list(range(100))
    shuffle(nums)
    sort_nums = merge_sort(nums)
    print(sort_nums)

