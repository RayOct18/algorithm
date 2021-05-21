

class BSTNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if self.val is None or self.val == val:
            self.val = val
        elif val < self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = BSTNode(val)
        elif val > self.val:
            if self.right:
                self.right.insert(val)
            else:
                self.right = BSTNode(val)
        return None

    def get_min(self):
        curr = self
        while curr.left:
            curr = curr.left
        return curr.val

    def get_max(self):
        curr = self
        while curr.right:
            curr = curr.right
        return curr.val

    def delete_min(self):
        if self is None:
            return None
        else:
            curr = self
            while curr.left and curr.left.left:
                curr = curr.left
            if curr.left and curr.left.right:
                curr.left = curr.left.right
            else:
                curr.left = None
            return curr

    def __str__(self):
        return f'(val:{self.val}, right:{self.right}, left:{self.left})'

if __name__ == '__main__':
    #ls = [4,3,5,1,2,6,7]
    #ls = [1,2,3,4,5,6,7]
    ls = [7,6,5,4,3,2,1]
    bst = BSTNode()
    for i in ls:
        bst.insert(i)
    print(bst)
    print(bst.get_min())
    print(bst.get_max())
    print(bst.delete_min())
    print(bst.get_min())
