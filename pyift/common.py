import math
INFINITY = float('inf')


def euclidean_distance(tuple1, tuple2):
    s = 0
    for i in range(len(tuple1)):
        s += (tuple1[i] - tuple2[i])**2
    return math.sqrt(s)

if __name__ == "__main__":
    print euclidean_distance((0, 0, 1), (1, 1, 1))
