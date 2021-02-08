import dataclasses


@dataclasses.dataclass(init=True, repr=True, eq=True, order=True, frozen=False)
class Dod:
    a: int
    b: int
    c: int = dataclasses.field(init=False)
    d: dataclasses.InitVar[float] = 2.0

    def __post_init__(self, d):
        print(d, self.d)
        self.c = self.a + self.b * d

    def __eq__(self, other):
        return isinstance(other,Dod)  and self.a == other.a

    def __hash__(self):
        return hash((self.a, self.b, self.c))


x = Dod(322,3232,32)
print(x.__hash__())
x1 = Dod(322,23432)
print(x1 == x)
print(x.__dict__)
