#!/usr/bin/python
import math
import pyift.queue as Queue
import pyift.adjacency as Adjacency
import pyift.image as Image
import pyift.common as Common

# F(<trivial>) = 0
# F(<path_extension>) = euclidean_distance(q, root(p))
# Min(Paths_t). Minimize all the paths ending in a given pixel t.

# Creating a simple binary image of size 6 x 6.
# Image is an array not an matrix.
orig = Image.Image(6, 6, 1)
orig.create_simple_image()
# print orig
# 0   0   0   0   0   0
# 0   1   1   1   0   0
# 0   1   0   1   0   0
# 0   1   0   1   0   0
# 0   1   1   1   0   0
# 0   0   0   0   0   0

# Distance array with INFINITY assigned to each pixel.
distance = Image.Image(orig.xsize, orig.ysize, orig.zsize)
distance.assign(Common.INFINITY)

# Root array with 'available' assigned to each pixel.
roots = Image.Image(orig.xsize, orig.ysize, orig.zsize)
roots.assign(Common.INFINITY)

# Adjacency Relation. 8-neighbour displacement array crated.
A = Adjacency.Adjacency()
A.circular(orig, math.sqrt(2))

# Queue. Implemented as a Heap, which is O(n log n).
Q = Queue.Queue()

# Trivial initialization of border pixels
for i, pixel in enumerate(orig.val):
    if pixel is not 0:  # If it is a border pixel
        distance.val[i] = 0  # The distance to the closet border pixel is 0.
        roots.val[i] = i     # You are the closest border pixel.
        Q.insert(i)          # Go to the queue for propagation.


# While there are still pixels to be processed
while not Q.empty():

    p = Q.remove()  # Remove a pixel (p)

    for adj in A.adj[1:]:   # Traverse through its neighbours
        q = p + adj         # Get the neighbour index position in the array (q)
        if orig.valid_index(q):  # If the neighbour is inside the image

            # Cost function for path extension.
            tmp = Common.euclidean_distance(orig.xyz_coord(roots.val[p]),
                                            orig.xyz_coord(q))

            # If the new cost is smaller then the current cost of my neighbor
            if tmp < distance.val[q]:
                # If my neighbour is in the queue,
                # I must remove it to avoid duplciates.
                if distance.val[q] != Common.INFINITY:
                    Q.remove_elem(q)

                # The new distace of my neighbor is the cost function extension
                distance.val[q] = tmp

                # The closest border of my neighbor is the same as mine
                roots.val[q] = roots.val[p]

                # Keep propagating.
                Q.insert(q)


print distance
# 1.4   1.0   1.0   1.0   1.4   2.2
# 1.0   0.0   0.0   0.0   1.0   2.0
# 1.0   0.0   1.0   0.0   1.0   2.0
# 1.0   0.0   1.0   0.0   1.0   2.0
# 1.0   0.0   0.0   0.0   1.0   2.0
# 1.4   1.0   1.0   1.0   1.4   2.2
