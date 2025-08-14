from dataclasses import dataclass, field

class Subject:
    """Represents what is being observed"""

    def __init__(self):
        self._observers = []

    def notify(self, modifier=None):
        """Alert the observers"""
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

    def attach(self, observer):
        """Add observer if not already in list"""
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        """Remove observer from list"""
        try:
            self._observers.remove(observer)
        except ValueError:
            pass


@dataclass
class Data(Subject):
    """Monitor the object"""
    name: str = ''
    _data: int = field(default=0, init=False)

    def __post_init__(self):
        super().__init__()  # initialize Subject part

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.notify()


@dataclass
class HexViewer:
    def update(self, subject):
        print(f'HexViewer: Subject {subject.name} has data 0x{subject.data:x}')


@dataclass
class OctalViewer:
    def update(self, subject):
        print(f'OctalViewer: Subject {subject.name} has data {oct(subject.data)}')


@dataclass
class DecimalViewer:
    def update(self, subject):
        print(f'DecimalViewer: Subject {subject.name} has data {subject.data}')


if __name__ == "__main__":
    obj1 = Data('Data 1')
    obj2 = Data('Data 2')

    view1 = DecimalViewer()
    view2 = HexViewer()
    view3 = OctalViewer()

    obj1.attach(view1)
    obj1.attach(view2)
    obj1.attach(view3)

    obj2.attach(view1)
    obj2.attach(view2)
    obj2.attach(view3)

    obj1.data = 10
    obj2.data = 15
