from random import shuffle


def insertion_sort(nums):
    nl = len(nums)
    for i in range(1, nl):
        key = nums[i]
        for j in reversed(range(i)):
            if nums[j] < key:
                j += 1
                break
        insert_num = nums.pop(i)
        nums.insert(j, insert_num)
    return nums


if __name__ == '__main__':
    nums = list(range(10))
    shuffle(nums)
    print(nums)

    sorted_nums = insertion_sort(nums)
    print(sorted_nums)
