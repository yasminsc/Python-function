class Dot:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2

    def equal(self, dot):
        return self.x1 == dot.x1 and self.x2 == dot.x2
