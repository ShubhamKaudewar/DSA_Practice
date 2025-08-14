from dataclasses import dataclass

@dataclass
class WrittenText:
    """Represents a Written text"""
    text: str

    def render(self) -> str:
        return self.text

@dataclass
class UnderlineWrapper:
    """Wraps a tag in <u>"""
    wrapped: WrittenText

    def render(self) -> str:
        return f"<u>{self.wrapped.render()}</u>"

@dataclass
class ItalicWrapper:
    """Wraps a tag in <i>"""
    wrapped: WrittenText

    def render(self) -> str:
        return f"<i>{self.wrapped.render()}</i>"

@dataclass
class BoldWrapper:
    """Wraps a tag in <b>"""
    wrapped: WrittenText

    def render(self) -> str:
        return f"<b>{self.wrapped.render()}</b>"


if __name__ == '__main__':
    before_gfg = WrittenText("GeeksforGeeks")
    after_gfg = ItalicWrapper(UnderlineWrapper(BoldWrapper(before_gfg)))

    # print("before:", before_gfg.render())
    print("after:", after_gfg.render())
