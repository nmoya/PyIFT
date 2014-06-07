class Image():
    """Image is a list of values"""
    def __init__(self, xsize, ysize, zsize):
        self.val = [0 for i in range(xsize * ysize * zsize)]
        self.xsize = xsize
        self.ysize = ysize
        self.zsize = zsize

    def __repr__(self):
        img = ''
        if self.n() <= 100 and self.zsize == 1:
            for i, px in enumerate(self.val):
                # x, y = self.x_coord(i), self.y_coord(i)
                if i % self.xsize == 0 and i != 0:
                    img += "\n"
                img += str(self.val[i]) + " "
            img += "\n"
        img += "(%d, %d, %d)\n" % (self.xsize, self.ysize, self.zsize)
        img += "N: %d" % (self.n())
        return img

    def create_simple_image(self):
        self.val = [0, 0, 0, 0, 0,
                    0, 1, 1, 1, 0,
                    0, 1, 0, 1, 0,
                    0, 1, 1, 1, 0,
                    0, 0, 0, 0, 0]
        self.zsize = 1
        self.xsize = 5
        self.ysize = 5

    def valid_index(self, index):
        if index >= 0 and index < self.n():
            return True
        return False

    def assign(self, value):
        self.val = [value for i in range(self.n())]

    def x_coord(self, idx):
        return (idx % (self.xsize * self.ysize)) % self.xsize

    def y_coord(self, idx):
        return (idx % (self.xsize * self.ysize)) / self.xsize

    def z_coord(self, idx):
        return (idx / (self.xsize * self.ysize))

    def xyz_coord(self, idx):
        return (self.x_coord(idx), self.y_coord(idx), self.z_coord(idx))

    def n(self):
        return len(self.val)


if __name__ == "__main__":
    pass
