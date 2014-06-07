#!/usr/bin/python
import math
import pyift.queue as Queue
import pyift.adjacency as Adjacency
import pyift.image as Image
import pyift.common as Common

orig = Image.Image(5, 5, 1)
orig.create_simple_image()

distance = Image.Image(orig.xsize, orig.ysize, orig.zsize)
distance.assign(Common.INFINITY)

A = Adjacency.Adjacency()
A.circular(orig, 1)

Q = Queue.Queue()
for i, pixel in enumerate(orig.val):
    if pixel is not 0:
        Q.insert(i)
        distance.val[i] = 0

while not Q.empty():
    p = Q.remove()
    for adj in A.adj[1:]:
        q = p + adj
        if not orig.valid_index(q):
            continue
        if distance.val[q] > distance.val[p]:
            tmp = Common.euclidean_distance(orig.xyz_coord(p),
                                            orig.xyz_coord(q))
            if tmp < distance.val[q]:
                if distance.val[q] != Common.INFINITY:
                    Q.remove_elem(q)
                distance.val[q] = tmp
                Q.insert(q)

print distance
