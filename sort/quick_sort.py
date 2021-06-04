

def partition(l, h, nums):
    pivot = nums[l]
    i, j = l+1, h-1
    while (i < j):
        while nums[i] <= pivot:
            i += 1
        while nums[j] > pivot:
            j -= 1
        if (i < j):
            nums[i], nums[j] = nums[j], nums[i]
    nums[l], nums[j] = nums[j], nums[l]
    return j

def quick_sort(nums, l, h):
    if (l < h):
        j = partition(l, h, nums)
        quick_sort(nums, l, j)
        quick_sort(nums, j+1, h-1)


if __name__ == '__main__':
    nums = [8, 1, 3, 2, 4, 6, 7, 9, 11, 16, 5]
    nums.append(float('inf'))
    quick_sort(nums, 0, len(nums))
    print(nums[:-1])