

class Heap():
    def __init__(self, nums, size=0, max_heap=True):
        self.nums = nums
        self.size = len(nums)
        self.is_max = max_heap
        
    def index(self, cur_node):
        parent = int((cur_node - 1) / 2)
        if cur_node == 0: parent = None
        left = cur_node * 2 + 1
        if left >= self.size: left = None
        right = cur_node * 2 + 2
        if right >= self.size: right = None
        return parent, left, right

    def heap(self, use_heapfiy=False):
        if not use_heapfiy:
            for i in range(self.size):
                self.compare_up(i)
        else:
            for i in range(self.size-1, -1, -1):
                self.heapify(i)
    
    def condition_up(self, parent, i):
        cond = (self.nums[parent] < self.nums[i])
        if not self.is_max:
            cond = not cond
        return cond

    def condition_down(self, i, left, right):
        if self.is_max:
            index = left if self.nums[left] > self.nums[right] else right
            cond = (self.nums[index] > self.nums[i])
        else:
            index = left if self.nums[left] < self.nums[right] else right
            cond = (self.nums[index] < self.nums[i])
        return (cond, index)

    def compare_up(self, i):
        parent, _, _ = self.index(i)

        while parent is not None and self.condition_up(parent, i):
            self.nums[i], self.nums[parent] = self.nums[parent], self.nums[i]
            i = parent
            parent, _, _ = self.index(i)

    def heapify(self, i):
        _, left, right = self.index(i)
        cond = True

        while (left and right) is not None and cond:
            cond, ind = self.condition_down(i, left, right)
            if cond:
                self.nums[i], self.nums[ind] = self.nums[ind], self.nums[i]
                i = ind
                _, left, right = self.index(i)

    def insert(self, num):
        self.nums.append(num)
        self.size += 1
        self.compare_up(self.size - 1)
    
    def delete(self):
        if self.size == 0:
            raise ValueError('heap is empty')
        last = self.size - 1
        self.nums[0], self.nums[last] = self.nums[last], self.nums[0]
        self.size -= 1
        self.heapify(0)
    
    def sort(self):
        while self.size > 0:
            self.delete()
        if self.is_max and self.nums[0] > self.nums[1]:
            self.nums[0], self.nums[1] = self.nums[1], self.nums[0]
        elif not self.is_max and self.nums[0] < self.nums[1]:
            self.nums[0], self.nums[1] = self.nums[1], self.nums[0]



if __name__ == '__main__':
    import random
    ls = [1,2,3,4,5,6,7,8,9]

    print('======Max Heap======')
    print(f'Input list: {ls}')
    heap = Heap(ls, max_heap=True)
    heap.heap()
    print(f'Max heap: {heap.nums}')
    heap.insert(9)
    print(f'Insert: {heap.nums}, Size: {heap.size}')
    heap.delete()
    print(f'Delete: {heap.nums}')
    heap.sort()
    print(f'Heap sort: {heap.nums}, Size: {heap.size}')

    ls = [9,8,7,6,5,4,3,2,1]
    print('======Min Heap======')
    print(f'Input list: {ls}')
    heap = Heap(ls, max_heap=False)
    heap.heap()
    print(f'Min heap: {heap.nums}')
    heap.insert(-1)
    print(f'Insert: {heap.nums}')
    heap.delete()
    print(f'Delete: {heap.nums}')
    heap.sort()
    print(f'Heap sort: {heap.nums}, Size: {heap.size}')

