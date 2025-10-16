class DetectSquares:

    def __init__(self):
        self.points = {}


    def add(self, point: list[int]) -> None:
        x, y = point
        self.points[(x, y)] = self.points.get((x, y), 0) + 1
        

    def count(self, point: list[int]) -> int:
        res = 0
        qx, qy = point
        for p in self.points:
            if abs(qx - p[0]) == abs(qy - p[1]) and p[0] != qx and p[1] != qy:
                res += self.points.get((qx, p[1]), 0) * self.points.get((p[0], qy), 0) * self.points.get(p)
        return res
                
detectSquares = DetectSquares()
detectSquares.add([3, 10])
detectSquares.add([11, 2])
detectSquares.add([3, 2])

print(detectSquares.count([11, 10]))