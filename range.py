

class Range:
    def __init__(self, start, end=None, step=1):
        if step == 0:
            raise ValueError('step cannot be 0.')

        if end is None:
            start, end = 0, start

        self._start = start
        self._step = step
        self._end = end

        end = end - 1 if end > 0 else end + 1
        self._length = (end - start) // step + 1

    def __len__(self):
        return self._length

    def __getitem__(self, k):
        if k < 0:
            k += self._length

        if not 0 <= k < self._length:
            raise IndexError('index out of range.')

        return self._start + k * self._step

    def __str__(self):
        return f'range({self._start}, {self._end}, {self._step})'

        
if __name__ == '__main__':
    R = Range(1, 4, 3)
    r = range(1, 4, 3)


    assert len(R) == len(r)

    for i, val in enumerate(r):
        assert R[i] == val
