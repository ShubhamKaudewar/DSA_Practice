import heapq

def customer_service(orders, k, w):
    n = len(orders)
    # Min heap
    placed_orders = []  # (order_duration, order_time, order_index)
    current_time = 0
    next_order_index = 0

    order_cost = [0] * n

    while next_order_index < n or placed_orders:
        # Push the orders available at current_time to the heap
        while next_order_index < n and current_time >= orders[next_order_index][0]:
            order_duration = orders[next_order_index][1]
            order_time = orders[next_order_index][0]
            order_index = next_order_index
            heapq.heappush(placed_orders, (order_duration, order_time, order_index))
            next_order_index += 1

        # If nothing available at current time
        if not placed_orders:
            current_time = orders[next_order_index][0]
            continue

        # Handle next order
        next_order = heapq.heappop(placed_orders)
        wait_time = current_time - next_order[1]
        prep_time = next_order[0]
        order_index = next_order[2]

        order_cost[order_index] = max(k * prep_time - w * wait_time, 0)
        current_time += prep_time

    return order_cost


def main():
    t = int(input())
    for _ in range(t):
        n, k, w = map(int, input().split())
        orders = []
        for _ in range(n):
            order_time, order_duration = map(int, input().split())
            orders.append([order_time, order_duration])

        costs = customer_service(orders, k, w)
        print(" ".join(map(str, costs)))


if __name__ == "__main__":
    main()
