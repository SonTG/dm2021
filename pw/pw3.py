import utils
from point import Point, getDist
from cluster import Cluster

# Hierarchical clustering


clusters = []

# read input, parse linecound words
wc = utils.loadData()

# make each point a cluster
for wcpoint in wc:
    c = Cluster(max)
    c.addPoint(Point(wcpoint))
    clusters.append(c)

print("before clustering")
print(clusters)

# start merging
idx = 0
while True:
    # calc distance between cluster pairs
    distances = []
    for c1 in clusters:
        for c2 in clusters:
            if c1 != c2:
                dist = c1.dist(c2)
                # DUP!, deal with it later
                distances.append(
                    { 
                        "c1": c1, 
                        "c2": c2,
                        "dist": dist
                    }
                )

    # find the smallest distance
    minDist = min(distances, key = getDist)
    
    # merge c1 and c2
    minDist["c1"].merge(minDist["c2"])
    clusters.remove(minDist["c2"])
    idx = idx + 1
    print(f"Iteration {idx} (#{len(clusters)}) {clusters}")    
    if len(clusters) == 1:
        print("Only one cluster left. Stop.")
        break

    

    