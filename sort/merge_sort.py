from random import shuffle


def merge_sort(nums):
    if len(nums) == 1:
        return 0

    half = len(nums) // 2
    left = nums[:half]
    right = nums[half:]

    merge_sort(right)
    merge_sort(left)

    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if right[j] > left[i]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1

    return nums


if __name__ == '__main__':
    nums = list(range(100))
    shuffle(nums)
    print(nums)

    sorted_nums = merge_sort(nums)
    print(sorted_nums)

'''
Sample Code

[3, 6, 1, 4, 9, 0, 8]
[3, 6, 1,| 4, 9, 0, 8]
[3,| 6, 1,| 4, 9, 0, 8]
[3,| 6,| 1,| 4, 9, 0, 8]

'''
