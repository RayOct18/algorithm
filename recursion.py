

def draw(h):
    if h == 0:
        return 0;

    draw(h-1)

    print('#' * h)

if __name__ == '__main__':
    draw(5)
