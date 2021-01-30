

class Vector(object):
    """Represent a vector in a multidimensional space."""

    def __init__(self, n):
        """Create n-dimensional vector of zeros."""
        self._coords = [0] * n

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        self._coords[j] =  val

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('dimension must agree.')
        result = Vector(len(self))
        for i, (s, o) in enumerate(zip(self, other)):
            result[i] = s + o
        return result

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('dimension must agree.')
        result = Vector(len(self))
        for i, (s, o) in enumerate(zip(self, other)):
            result[i] = s - o
        return result

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other


if __name__ == '__main__':
    v = Vector(5)
    v[1] = 23
    v[-1] = 45
    print(v[4])
    u = v + v
    print(u)
    u = v - v
    print(u)
    total = 0
    for entry in v:
        total += entry
    print(total)
    print(u)
    print(v)
    print(u == v)
    print(u != v)
