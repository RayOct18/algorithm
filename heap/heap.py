

class Heap():
    def __init__(self, nums, size=0, max_heap=True):
        self.nums = nums
        self.size = len(nums)
        self.is_max = max_heap
        
    def index(self, cur_node):
        parent = int((cur_node - 1) / 2)
        if parent < 0: parent = None
        left = cur_node * 2 + 1
        if left >= len(self.nums): left = None
        right = cur_node * 2 + 2
        if right >= len(self.nums): right = None
        return parent, left, right

    def heap(self):
        for i in range(self.size):
            if self.is_max:
                self.max_heap(i)
            else:
                self.min_heap(i)

    def min_heap(self, i):
        nums = self.nums
        parent, right, left = self.index(i)

        while parent is not None and nums[parent] > nums[i]:
            nums[i], nums[parent] = nums[parent], nums[i]
            i = parent
            parent, right, left = self.index(i)

    def max_heap(self, i):
        nums = self.nums
        parent, right, left = self.index(i)

        while parent is not None and nums[parent] < nums[i]:
            nums[i], nums[parent] = nums[parent], nums[i]
            i = parent
            parent, right, left = self.index(i)

    def insert(self, num):
        self.nums.append(num)
        self.size = len(self.nums)
        if self.is_max:
            self.max_heap(self.size - 1)
        else:
            self.min_heap(self.size - 1)
                

if __name__ == '__main__':
    ls = [1,2,3,4,5,6,7,8]
    heap = Heap(ls, max_heap=True)
    heap.heap()
    print(heap.nums)
    heap.insert(9)
    print(heap.nums)

    heap = Heap(ls, max_heap=False)
    heap.heap()
    print(heap.nums)
    heap.insert(-1)
    print(heap.nums)

