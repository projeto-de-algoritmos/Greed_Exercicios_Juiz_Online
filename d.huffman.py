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

    

    custom_queries_list = custom_queries.sort(key=lambda query: (query.left, query.right))

    left_index = 0
    right_index = -1
    bucket_frequencies = [0] * SQRT
    frequencies = [0] * MAX_VAL
    geq_root = set()
    bucket_frequencies[0] = n

    for query_index in range(m):
        custom_query = custom_queries_list[query_index]
        if custom_query.left == custom_query.right:
            continue

        while right_index < custom_query.right:
            right_index += 1
            custom_add(array[right_index], frequencies, bucket_frequencies, geq_root)
        while left_index > custom_query.left:
            left_index -= 1
            custom_add(array[left_index], frequencies, bucket_frequencies, geq_root)
        while right_index > custom_query.right:
            custom_remove(array[right_index], frequencies, bucket_frequencies, geq_root)
            right_index -= 1
        while left_index < custom_query.left:
            custom_remove(array[left_index], frequencies, bucket_frequencies, geq_root)
            left_index += 1

        result = 0
        priority_queue = [frequencies[val] for val in geq_root]
        priority_queue.sort()

        current_frequencies = bucket_frequencies[:]

        leftover = -1
        for i in range(1, SQRT):
            here = current_frequencies[i]
            if here == 0:
                continue

            if leftover != -1:
                new_value = leftover + i
                result += new_value

                if new_value >= SQRT:
                    priority_queue.append(new_value)
                else:
                    current_frequencies[new_value] += 1

                leftover = -1
                here -= 1

            if here & 1 == 1:
                leftover = i
                here -= 1

            result += i * here
            new_value = i * 2

            if new_value >= SQRT:
                priority_queue.extend([new_value] * (here >> 1))
            else:
                current_frequencies[new_value] += here >> 1

        if leftover != -1:
            priority_queue.append(leftover)

        heapq.heapify(priority_queue)

        while len(priority_queue) > 1:
            a = heapq.heappop(priority_queue)
            b = heapq.heappop(priority_queue)
            result += a + b
            heapq.heappush(priority_queue, a + b)

        results[custom_query.id] = result

    return results

n_input = int(input())
array_input = list(map(int, input().split()))
m_input = int(input())
queries_input = [tuple(map(int, input().split())) for _ in range(m_input)]

output_result = custom_huffman_coding(n_input, array_input, m_input, queries_input)

for answer in output_result:
    print(answer)
