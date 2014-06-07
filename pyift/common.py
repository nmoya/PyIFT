import math
INFINITY = 2147483647


def euclidean_distance(tuple1, tuple2):
    s = 0
    for i in range(len(tuple1)):
        s += math.pow((tuple1[i] - tuple2[i]), 2)
    return s
