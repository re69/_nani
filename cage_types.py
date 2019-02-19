class __BaseType:
    def __init__(self, title: str):
        self.title = title

    def __str__(self):
        raise NotImplementedError


class _Wall(__BaseType):
    def __init__(self):
        super().__init__('wall')

    def __str__(self):
        return '▉'


class _Empty(__BaseType):
    def __init__(self):
        super().__init__('empty')

    def __str__(self):
        return '░'


class CageType:
    Empty = _Empty()
    Wall = _Wall()
    _types = [Empty, Wall]

    @staticmethod
    def by_char(char: str):
        for cage_type in CageType._types:
            if cage_type.__str__() == char:
                return cage_type
        return CageType.Empty
