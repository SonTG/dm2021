import utils
import random
from point import Point, getDist
from cluster import Cluster


# read input, parse linecound words
wc = utils.loadData()

# use Point class as wrapper
points = [Point(wcpoint) for wcpoint in wc]
print(points)

# randomly select centroid
K = 3
centroids = [ random.choice(points) for i in range(0, K) ]
print(f"Initial centroids: {centroids}")

 # iterate until centroids converges
while True:
    # initialize empty clusters
    clusters = [Cluster() for i in range(0, K)]
    
    for p in points:
        # find the smallest distance to the clusters
        distances = [p.dist(centroid) for centroid in centroids]        
        argmin = distances.index(min(distances))

        # add this point to that cluster
        clusters[argmin].addPoint(p)
    
    print(clusters)

    # find centroids
    newCentroids = [Point(c.getCentroid()) for c in clusters]#
    print(f"Centroids: {newCentroids}")
    
    # check the convergence
    centroidDiffs = []
    for c1, c2 in zip(centroids, newCentroids):
        centroidDiffs.append(c1.dist(c2))
    sse = 0
    for diff in centroidDiffs:
        sse += diff ** 2
    print(f"SSE: {sse}")

    if sse < 1:
        print("Centroids do not move. Stop.")
        break

    # update centroids
    centroids = newCentroids        



