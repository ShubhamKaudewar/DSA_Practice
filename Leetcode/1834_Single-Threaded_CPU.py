from typing import List
import pytest
import heapq
from collections import defaultdict

class Solution:
    """
    This question requires understanding of Shortest Job First (SJF) scheduling algorithm
    This requires to use 2 priority queues when necessery
    """
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Pair tasks with original indices and sort by enqueue time
        indexed_tasks = sorted((enqueue, process, idx) for idx, (enqueue, process) in enumerate(tasks))

        time = 0
        ptr = 0
        heap = []
        ans = []
        n = len(tasks)

        while ptr < n or heap:
            # If heap is empty, jump time to next task's enqueue time
            if not heap:
                time = max(time, indexed_tasks[ptr][0])

            # Add all tasks that are available by current time
            while ptr < n and indexed_tasks[ptr][0] <= time:
                enqueue, process, idx = indexed_tasks[ptr]
                heapq.heappush(heap, (process, idx))
                ptr += 1

            # Process the best task
            process, idx = heapq.heappop(heap)
            time += process
            ans.append(idx)

        return ans

    def getOrder1(self, tasks: List[List[int]]) -> List[int]:
        """
        Below code is mine but gives TLE because we are checking time + 1 so instead we need to check for if cpu idle
        jump to next enqueueTime
        """
        avail_task_map = defaultdict(list)
        for idx, task in enumerate(tasks):
            avail_task_map[task[0]].append(idx)

        time = 0
        cpu_avail_at = 0
        avail_task_queue = []
        ans = []
        while avail_task_map:
            if time == cpu_avail_at:
                cpu_avail_at = 0

            # Check if any task available at that time
            if time in avail_task_map:
                # Find all available task time and prioritize based on minimal process time
                for task_idx in avail_task_map[time]:
                    task = tasks[task_idx]
                    heapq.heappush(avail_task_queue, (task[-1], task_idx, task[0]))

            if avail_task_queue and cpu_avail_at == 0:
                processTime, idx, startTime = heapq.heappop(avail_task_queue)
                cpu_avail_at = time + processTime
                # Remove consumed task
                avail_task_map[startTime].remove(idx)
                if not avail_task_map[startTime]:
                    del avail_task_map[startTime]
                ans.append(idx)
            time += 1
        return ans



def test_case_1():
    sol = Solution()
    tasks = [[1,2],[2,4],[3,2],[4,1]]
    actual = sol.getOrder(tasks)
    expected = [0,2,3,1]
    assert actual == expected

def test_case_2():
    sol = Solution()
    tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
    actual = sol.getOrder(tasks)
    expected = [4,3,2,0,1]
    assert actual == expected

def test_case_3():
    sol = Solution()
    tasks = [[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]]
    actual = sol.getOrder(tasks)
    expected = [6,1,2,9,4,10,0,11,5,13,3,8,12,7]
    assert actual == expected

if __name__ == '__main__':
    pytest.main()