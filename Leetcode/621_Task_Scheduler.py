import pytest
from typing import Optional, List
import heapq, math
from collections import defaultdict, Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_heap = [-count for count in task_counts.values()]  # Max heap (negative values for heapq)
        heapq.heapify(max_heap)

        queue = deque()  # Queue to store tasks in cooldown
        time = 0

        while max_heap or queue:
            time += 1
            if max_heap:
                freq = heapq.heappop(max_heap) + 1  # Process task, decrement frequency
                if freq < 0:
                    queue.append((freq, time + n))  # Store in cooldown

            # Release tasks from cooldown
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])

        return time
        
    # Below solution is not very optimized
    def decrement(self, idle):
        for k in list(idle.keys()):
            if idle[k] > 0:
                idle[k] -= 1
                
            if idle[k] == 0:
                del idle[k]
        return idle

    def leastInterval2(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        heap = [(v, k) for k, v in dict(c).items()]
        heapq.heapify(heap)

        sequence = []
        idle_state = defaultdict(lambda: 0)

        while heap:
            for i in range(1, len(heap)+1):
                get_task = heapq.nlargest(i, heap)[0]
                freq, task = get_task
                all_idle = False
                
                if task in idle_state:
                    last_heap = heap.copy()
                    while heap:
                        get_task = heapq.heappop(heap)
                        freq, task = get_task
                        if task in idle_state:
                            continue
                        break
                    
                    if not heap:
                        all_idle = True
                    heap = last_heap
                    heapq.heapify(heap)
                        
                if all_idle:
                    sequence.append("idle")
                else:
                    sequence.append(task)
                    idle_state[task] = n+1
                    
                    if freq-1 == 0:
                        del heap[heap.index(get_task)]
                        heapq.heapify(heap)
                    else:
                        heap[heap.index(get_task)] = tuple((freq-1, task))
                        heapq.heapify(heap)
                self.decrement(idle_state)
        return len(sequence)

# def test_case_1():
#     sol = Solution()
#     tasks = ["A","A","A","B","B","B"]
#     n = 2
#     actual = sol.leastInterval(tasks, n)
#     expected = 8
#     assert actual == expected
# 
# def test_case_2():
#     sol = Solution()
#     tasks = ["A","C","A","B","D","B"]
#     n = 1
#     actual = sol.leastInterval(tasks, n)
#     expected = 6
#     assert actual == expected
# 
# def test_case_3():
#     sol = Solution()
#     tasks = ["A","A","A","B","B","B"]
#     n = 3
#     actual = sol.leastInterval(tasks, n)
#     expected = 10
#     assert actual == expected

def test_case_4():
    sol = Solution()
    tasks = ["B","C","D","A","A","A","A","G"]
    n = 1
    actual = sol.leastInterval(tasks, n)
    expected = 8
    assert actual == expected

if __name__ == '__main__':
    pytest.main()