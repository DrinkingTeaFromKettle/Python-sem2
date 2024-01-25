class Prostokat:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def obwod(self):
        return 2 * (self.a + self.b)
    def pole(self):
        return self.a * self.b