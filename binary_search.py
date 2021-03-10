
def binary_search(data, target, low, high):
    if low > high:
        return False
    mid = (low + high) // 2
    if data[mid] > target:
        return binary_search(data, target, low, mid-1)
    elif data[mid] < target:
        return binary_search(data, target, mid+1, high)
    else:
        return True

if __name__ == '__main__':
    data = [1,3,5,6,8,9]
    status = binary_search(data, 8, 0, 5)
    print(status)
