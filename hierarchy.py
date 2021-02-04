

class Progression:
    def __init__(self, start=0):
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            ans = self._current
            self._advance()
            return ans

    def __iter__(self):
        return self

    def print_progression(self, n):
        print(' '.join(str(next(self)) for _ in range(n)))

class ArithmeticProgression(Progression):
    def __init__(self, increment=1, start=0):
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        self._current += self._increment



if __name__ == '__main__':
    p = Progression()
    p.print_progression(10)

    a = ArithmeticProgression(5)
    a.print_progression(10)

