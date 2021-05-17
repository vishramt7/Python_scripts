
class CountFromBy:
    def __repr__ (self) -> str:
        return str(self.val)

    def __init__ (self, v:int=0, i:int=1) -> None:
        self.val = v
        self.incr = i

    def increase (self) -> None:
        self.val += self.incr


a = CountFromBy(100,10)
print (a.val, a.incr, a)

a.increase()
print (a.val)

b = CountFromBy()
b.increase()
print (b)

c = CountFromBy(10,0.2)
c.increase()
print (c)
