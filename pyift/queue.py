import heapq


class Queue(object):
    """docstring for Queue"""
    def __init__(self):
        self.heap = []

    def __repr__(self):
        return ", ".join(map(str, self.heap))

    def insert(self, el):
        heapq.heappush(self.heap, el)

    def remove(self):
        return heapq.heappop(self.heap)

    def remove_min(self):
        return heapq.heappop(self.heap)

    def remove_elem(self, elem):
        try:
            self.heap.remove(elem)
        except ValueError:
            pass

    def empty(self):
        if len(self.heap) == 0:
            return True
        return False


if __name__ == "__main__":
    pass
