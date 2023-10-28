import heapq

SQRT = 500
MAX_VAL = 100001

class CustomQuery:
    def __init__(self, left, right, identifier):
        self.left = left
        self.right = right
        self.id = identifier
        self.bucket = left // SQRT

    def __lt__(self, other):
        if self.bucket != other.bucket:
            return self.bucket < other.bucket
        return self.right < other.right

