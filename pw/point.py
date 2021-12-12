def getDist(d):
    return d["dist"]

class Point:
    # data point in review length has only 1 dimension
    def __init__(self, x) -> None:
        self.x = x
        #self.y = y
    
    def dist(self, anotherPoint):
        # L1 or L2?
        return abs(self.x - anotherPoint.x)

    def __repr__(self) -> str:
        return f"p{{{self.x}}}"