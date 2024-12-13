class SumFactorial:
    def __init__(self):
        self.fact = 1
        self.s = 0
        print(self.sum())
        print(self.factorial())

    def sum(self):
        for i in range(1, 101):
            self.s += i
        return self.s

    def factorial(self):
        for i in range(1, 11):
            self.fact *= i
        return self.fact


if __name__ == '__main__':
    SumFactorial()
