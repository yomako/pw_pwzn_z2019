"""
Uzupełnij klasę Calculator o obsługę wyjątków (1pkt).
Podnoszone wyjątki:
- błędna operacja - WrongOperation
- błędne argumenty (nie liczba) - NotNumberArgument
- pusta pamięć (zarówno przy pytaniu o pamięć
jak i operację z argumentem domyślnym) - EmptyMemory
- dzielenie przez zero jest przekształcane w CalculatorError
"""
from operator import add, mul, sub, truediv


class CalculatorError(Exception):
    pass


class WrongOperation(CalculatorError, Exception):
    pass


class NotNumberArgument(CalculatorError, Exception):
    pass


class EmptyMemory(CalculatorError, Exception):
    pass


class Calculator:
    operations = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': truediv,
    }

    def __init__(self):
        self._memory = None
        self._short_memory = None

    def run(self, operator, arg1, arg2=None):
        """
        Returns result of given operation.

        :param operator: sign of operation to perform
        :type operator: str
        :param arg1: first argument, must be a numeric value
        :type arg1: float
        :param arg2: optional, second argument, must be a numeric value
        :type arg2: float
        :return: result of operation
        :rtype: float
        """
        if operator in self.operations:
            arg2 = arg2 or self.memory
            if arg2 is None:
                raise EmptyMemory from ZeroDivisionError
            if arg2:
                try:
                    self._short_memory = self.operations[operator](arg1, arg2)
                    return self._short_memory
                except TypeError as exc:
                    raise NotNumberArgument() from exc
        else:
            raise WrongOperation()

    @property
    def memory(self):
        return self._memory

    def memorize(self):
        """Saves last operation result to memory."""
        self._memory = self._short_memory

    def clean_memory(self):
        """Cleans memorized value"""
        self._memory = None

    def in_memory(self):
        """Prints memorized value."""
        if self.memory is None:
            raise EmptyMemory()
        print(f"Zapamiętana wartość: {self.memory}")


if __name__ == '__main__':
    b = None
    calc = Calculator()

    try:
        b = calc.run('+', 1, 'a')
    except CalculatorError as exc:
        assert type(exc) == NotNumberArgument
        assert b is None

    try:
        b = calc.run('^', 2, 3)
    except CalculatorError as exc:
        assert type(exc) == WrongOperation
        assert b is None

    try:
        calc.in_memory()
    except CalculatorError as exc:
        assert type(exc) is EmptyMemory
    else:
        raise AssertionError

    try:
        b = calc.run('/', 2)
    except CalculatorError as exc:
        assert type(exc) == EmptyMemory
        assert b is None
    else:
        raise AssertionError

    try:
        b = calc.run('/', 1, 0)
    except CalculatorError as exc:
        assert type(exc.__cause__) == ZeroDivisionError
        assert b is None
    else:
        raise AssertionError
