class Plus:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return self.val + other.val


class Minus:
    def __init__(self, val):
        self.val = val

    def __sub__(self, other):
        return self.val - other.val


class Umno:
    def __init__(self, val):
        self.val = val

    def __mul__(self, other):
        return self.val * other.val


class Delenie:
    def __init__(self, val):
        self.val = val

    def __truediv__(self, other):
        return self.val / other.val


class Test(Plus, Minus, Umno, Delenie):
    def __init__(self, val):
        Plus.__init__(self, val)
        Minus.__init__(self, val)
        Umno.__init__(self, val)
        Delenie.__init__(self, val)


num1 = Test(543)
num2 = Test(4)

print(f'{num1 + num2}\n'
      f'{num1 - num2}\n'
      f'{num1 * num2}\n'
      f'{num1 / num2}\n')
