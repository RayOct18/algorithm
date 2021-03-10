
def draw_line(length, label=''):
    line = '-' * length
    if label:
        line += ' ' + label
    print(line)

def draw_interval(length):
    if length > 0:
        draw_interval(length-1)
        draw_line(length)
        draw_interval(length-1)


def draw_ruler(inch, length):
    draw_line(length, '0')
    for i in range(1, 1+inch):
        draw_interval(length - 1)
        draw_line(length, str(i))


if __name__ == '__main__':
    draw_ruler(2, 5)
