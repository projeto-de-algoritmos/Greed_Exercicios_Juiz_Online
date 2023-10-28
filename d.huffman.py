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

def custom_huffman_coding(n, array, m, custom_queries):
    results = [0] * m

    def custom_remove(value, frequencies, bucket_frequencies, geq_root):
        if frequencies[value] < SQRT:
            bucket_frequencies[frequencies[value]] -= 1
            frequencies[value] -= 1
            bucket_frequencies[frequencies[value]] += 1
        elif frequencies[value] == SQRT:
            geq_root.remove(value)
            bucket_frequencies[SQRT - 1] += 1
            frequencies[value] -= 1
        else:
            frequencies[value] -= 1

    def custom_add(value, frequencies, bucket_frequencies, geq_root):
        if frequencies[value] >= SQRT:
            frequencies[value] += 1
        elif frequencies[value] == SQRT - 1:
            bucket_frequencies[SQRT - 1] -= 1
            frequencies[value] += 1
            geq_root.add(value)
        else:
            bucket_frequencies[frequencies[value]] -= 1
            frequencies[value] += 1
            bucket_frequencies[frequencies[value]] += 1