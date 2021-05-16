from random import shuffle
from sorted_plot import plot_bar


def insertion(nums):
    for i in range(1, len(nums)):
        for j in range(i-1, -1, -1):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                i = j
                plot_bar(nums, i)
            else:
                break
    return nums
    

if __name__ == '__main__':
    nums = list(range(20))
    shuffle(nums)
    sort_nums = insertion(nums)
    print(sort_nums)
