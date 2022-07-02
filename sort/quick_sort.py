

def partition(nums, l, r):
    pivot = nums[r]
    i, j = l, r-1
    while (i < j):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        else:
            j -= 1
    if nums[j] < pivot:
        j += 1
    nums[r], nums[j] = nums[j], nums[r]
    return j

def quick_sort(nums, l, r):
    if (l < r):
        j = partition(nums, l, r)
        quick_sort(nums, l, j-1)
        quick_sort(nums, j+1, r)


if __name__ == '__main__':
    nums = [8, 1, 3, 2, 4, 6, 7, 9, 11, 16, 5]
    quick_sort(nums, 0, len(nums)-1)
    print(nums)

