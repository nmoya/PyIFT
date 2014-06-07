class Adjacency():
    """Adjacency is a list of displacements"""
    def __init__(self):
        self.adj = []

    def __repr__(self):
        return ", ".join(map(str, self.adj))

    def circular(self, img, radius):
        # Expand to work with arbitrary radius. Only 4 for now.
        self.adj = [0, 1, -img.xsize, -1, img.xsize]


if __name__ == "__main__":
    pass
