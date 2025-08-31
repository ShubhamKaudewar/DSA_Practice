import pytest
from collections import defaultdict
from typing import List

class DetectSquares:
    def __init__(self):
        self.points_map = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points_map[tuple(point)] += 1
        return None

    def count(self, point: List[int]) -> int:
        x, y = point
        total = 0

        for (px, py), freq_n1 in self.points_map.items():
            if py == y and px != x:
                side = abs(px - x)

                for dy in [side, -side]: # check on either side of point
                    nx, ny = x, y + dy
                    dx, dy = px, py + dy

                    freq_n2 = self.points_map.get((nx, ny), 0)
                    freq_diag = self.points_map.get((dx, dy), 0)

                    total += freq_n1 * freq_n2 * freq_diag  # all three frequencies now considered

        return total


def test_case_1():
    ds = None
    actions = ["DetectSquares","add","add","add","count","count","add","count"]
    values = [[],[[3,10]],[[11,2]],[[3,2]],[[11,10]],[[14,8]],[[11,2]],[[11,10]]]
    actual = [None]
    for action, point in zip(actions, values):
        if action == "DetectSquares":
            ds = DetectSquares()
            continue
        method = getattr(ds, action, None)
        if callable(method):
            actual.append(method(point[0]))
    expected = [None, None, None, None, 1, 0, None, 2]
    assert actual == expected

def test_case_2():
    ds = None
    actions = ["DetectSquares","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count"]
    values = [[],[[419,351]],[[798,351]],[[798,730]],[[419,730]],[[998,1]],[[0,999]],[[998,999]],[[0,1]],[[226,561]],[[269,561]],[[226,604]],[[269,604]],[[200,274]],[[200,793]],[[719,793]],[[719,274]],[[995,99]],[[146,948]],[[146,99]],[[995,948]],[[420,16]],[[962,558]],[[420,558]],[[962,16]],[[217,833]],[[945,105]],[[217,105]],[[945,833]],[[26,977]],[[26,7]],[[996,7]],[[996,977]],[[96,38]],[[96,483]],[[541,483]],[[541,38]],[[38,924]],[[961,1]],[[961,924]],[[38,1]],[[438,609]],[[818,609]],[[818,229]],[[438,229]]]
    actual = [None]
    for action, point in zip(actions, values):
        if action == "DetectSquares":
            ds = DetectSquares()
            continue
        method = getattr(ds, action, None)
        if callable(method):
            actual.append(method(point[0]))
    expected = [None,None,None,None,1,None,None,None,1,None,None,None,1,None,None,None,1,None,None,None,1,None,None,None,1,None,None,None,1,None,None,None,1,None,None,None,1,None,None,None,1,None,None,None,1]
    assert actual == expected



if __name__ == '__main__':
    pytest.main()