class demo:
    str = ["a", "b", 3, 3.5, "c"]

    def __init__(self):
        pass

    def firstMethod(self):
        for s in self.str:
            print(s)

    def secondMethod(self):
        for x in range(0, 5, 3):
            print(x)

    def thirdMethod(self, a, b):
        print(a, b)


ob = demo();
ob.thirdMethod("hello", 5)
