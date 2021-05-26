class Calculator(object):

    @classmethod
    def add(cls, num1: int, num2: int) -> int:
        return num1 + num2

    @classmethod
    def subtraction(cls, num1: int, num2: int) -> int:
        return num1 - num2

    @classmethod
    def multiplication(cls, num1: int, num2: int) -> int:
        return num1 * num2

    @classmethod
    def quotient(cls, num1: int, num2: int) -> int:
        return num1 // num2

    @staticmethod
    def take_care():
        weytin_mum_fit_get = Calculator.add
        mummy = "Mum pls give me addition"
        return mummy + " {} ".format(weytin_mum_fit_get)
