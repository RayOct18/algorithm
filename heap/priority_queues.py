from heap import Heap

class PriorityQueues(Heap):
    def __init__(self, ls, max_heap=True):
        super().__init__(ls, max_heap=max_heap)
        self.heap()

    def get(self):
        self.delete()
        return self.nums[self.size]

    def put(self, num):
        if self.empty:
            raise ValueError('queues is empty')

        if self.size < len(self.nums):
            self.size += 1
            self.nums[self.size-1] = num
            self.compare_up(self.size - 1)
        else:
            self.size += 1
            self.nums.append(num)
            self.compare_up(self.size - 1)
    
    def empty(self):
        return True if self.size == 0 else False

if __name__ == '__main__':
    ls = [1,2,3,4,5,6]
    max_p = PriorityQueues(ls, max_heap=True)
    print(max_p.nums)
    max_p.get()
    print(max_p.nums)
    max_p.put(7)
    print(max_p.nums)

    ls = [6,5,4,3,2,1]
    min_p = PriorityQueues(ls, max_heap=False)
    min_p.get()
    print(min_p.nums)
    min_p.put(-1)
    min_p.put(-2)
    print(min_p.nums)