from os import stat
import statistics

class Cluster:
    def __init__(self, distPolicy = min, centroidPolicy = statistics.mean):
        self.points = []
        self.distPolicy = distPolicy
        self.centroidPolicy = centroidPolicy

    def addPoint(self, p):
        self.points.append(p)
    
    def dist(self, anotherCluster):
        """
        Calculate distance between two clusters
        """
        d = 0
        if self.distPolicy == min:
            d = float("inf")
        else:
            d = -1
        for p1 in self.points:
            for p2 in anotherCluster.points:
                d = self.distPolicy(d, p1.dist(p2))
        return d

    def merge(self, anotherCluster):
        """
        Merge myself with another cluster. This should add all points from
        the other cluster to me. 
        The caller should delete the other cluster.         
        """
        self.points += anotherCluster.points
        anotherCluster.points = []


    def getCentroid(self):
        """
        Get centroid for current cluster
        """
        return self.centroidPolicy([p.x for p in self.points])


    def __repr__(self):
        return f"{[p.x for p in self.points]}"

