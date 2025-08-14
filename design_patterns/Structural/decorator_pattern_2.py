from dataclasses import dataclass
from typing import Callable

@dataclass
class UnderlineWrapper:
    """Wraps return value in <u>"""
    func: Callable

    def __call__(self):
        return f"<u>{self.func()}</u>"

@dataclass
class ItalicWrapper:
    """Wraps return value in <i>"""
    func: Callable

    def __call__(self):
        return f"<i>{self.func()}</i>"

@dataclass
class BoldWrapper:
    """Wraps return value in <b>"""
    func: Callable

    def __call__(self):
        return f"<b>{self.func()}</b>"


@ItalicWrapper
@UnderlineWrapper
@BoldWrapper
def get_text():
    return "GeeksforGeeks"


if __name__ == "__main__":
    print("before:", "GeeksforGeeks")
    print("after :", get_text())
