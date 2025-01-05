from typing import List
import pytest
from collections import defaultdict

class FreqStack:
    """This code logic is brilliently written and simple to understand
    self.group_map: Maintain frequency to value map
    self.freq_map: Maintain value to frequency map
    self.max_freq: Maintain max frequency present in val stack to pop
    """
    def __init__(self):
        self.freq_map = defaultdict(int)
        self.group_map = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq_map[val] += 1
        freq = self.freq_map[val]
        self.max_freq = max(self.max_freq, freq)
        self.group_map[freq].append(val)
        return None

    def pop(self) -> int:
        val = self.group_map[self.max_freq].pop()
        self.freq_map[val] -= 1
        if not self.group_map[self.max_freq]:
            self.max_freq -= 1
        return val

def test_case_1():
    actions = ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
    values = [[], [5], [7], [5], [7], [4], [5], [], [], [], []]
    expected = [None, None, None, None, None, None, None, 5, 7, 5, 4]
    output, fs = [], None
    for action, value in zip(actions, values):
        if action == "FreqStack":
            fs = FreqStack()
            output.append(None)
        elif action == "push":
            output.append(fs.push(*value))
        else:
            output.append(fs.pop(*value))
    assert output == expected

def test_case_2():
    actions = ["FreqStack","push","push","push","push","push","push","push","push","push","push","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop"]
    values = [[],[1],[0],[0],[1],[5],[4],[1],[5],[1],[6],[],[],[],[],[],[],[],[],[],[]]
    expected = [None,None,None,None,None,None,None,None,None,None,None,1,1,5,1,0,6,4,5,0,1]
    output, fs = [], None
    for action, value in zip(actions, values):
        if action == "FreqStack":
            fs = FreqStack()
            output.append(None)
        elif action == "push":
            output.append(fs.push(*value))
        else:
            output.append(fs.pop(*value))
    assert output == expected

if __name__ == '__main__':
    pytest.main()