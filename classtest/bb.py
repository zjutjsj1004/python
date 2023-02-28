from aa import Aa

class B:
    def __init__(self) -> None:
        self.age = 1
    def print_all(self):
        a = Aa("name1")
        print(a.name)


b = B()
print(b.print_all())