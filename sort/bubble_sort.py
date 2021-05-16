from random import shuffle


def buble_sort(nums):
    nl = len(nums) - 1
    for _ in range(nl):
        for i in range(nl):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums

if __name__ == '__main__':
    nums = range(10)
    shuffle(nums)
    print(nums)
    sorted_nums = buble_sort(nums)
    print(sorted_nums)
