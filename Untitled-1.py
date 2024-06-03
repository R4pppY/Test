class A:
    def info(self):
        print("Ini Class A")

class B(A):
    def info(self):
        print("Ini Class B")


class C(A):
    def info(self):
        print("Ini Class C")


class D(B):
    def info(self):
        print("Ini Class D")


class E(D,C):
    pass

objek = E()
objek.info()
help(objek)