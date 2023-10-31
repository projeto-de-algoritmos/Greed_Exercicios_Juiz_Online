class KnapsackSolver:
    def __init__(self):
        pass

    def solve(self):
        test_cases = int(input())

        for _ in range(test_cases):
            num_items, weight = map(int, input().split())
            items = list(map(int, input().split()))

            if min(items) > weight:
                print(-1)
                continue

            if weight % 2 == 0:
                mid_point = weight // 2
            else:
                mid_point = weight // 2 + 1

            if mid_point in items:
                print(1)
                print(items.index(mid_point) + 1)
                continue
            elif weight in items:
                print(1)
                print(items.index(weight) + 1)
                continue

            position = -1
            for i in range(num_items):
                if mid_point < items[i] < weight:
                    position = i + 1
                    break

            if position != -1:
                print(1)
                print(position)
                continue

            item_positions = {}
            total_weight = 0
            selected_items = []

            for i in range(num_items):
                if items[i] in item_positions:
                    item_positions[items[i]].append(i + 1)
                else:
                    item_positions[items[i]] = [i + 1]

            found_mid_point = 1
            for key in sorted(item_positions.keys()):
                for i in range(len(item_positions[key])):
                    total_weight += key
                    if total_weight < mid_point:
                        selected_items.append(item_positions[key][i])
                    if mid_point <= total_weight <= weight:
                        selected_items.append(item_positions[key][i])
                        found_mid_point = 0
                        break

            if found_mid_point == 1:
                print(-1)
                continue

            print(len(selected_items))
            print(*selected_items)


solver = KnapsackSolver()
solver.solve()