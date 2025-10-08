import pytest
from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        """This solution only work when there is fixed dominion of notes"""
        five, ten = 0, 0

        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            else:  # bill == 20
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True


    def lemonadeChange1(self, bills: List[int]) -> bool:
        cash = []

        for bill in bills:
            change = bill - 5

            # Try to give change using available cash
            temp = sorted(cash, reverse=True)  # Sort descending
            for note in temp:
                if change >= note:
                    change -= note
                    cash.remove(note)
                if change == 0:
                    break

            if change != 0:
                return False

            cash.append(bill)  # Add current bill to cash
        return True


def test_case_1():
    sol = Solution()
    bills = [5,5,5,10,20]
    actual = sol.lemonadeChange(bills)
    expected = True
    assert actual == expected

def test_case_2():
    sol = Solution()
    bills = [5,5,10,10,20]
    actual = sol.lemonadeChange(bills)
    expected = False
    assert actual == expected

if __name__ == '__main__':
    pytest.main()