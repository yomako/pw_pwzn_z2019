import pytest

from lab_11.tasks.tools.calculator import (
    Calculator,
    CalculatorError,
    EmptyMemory,
    NotNumberArgument,
    WrongOperation,
)


@pytest.fixture(scope='module')
def calculator():
    calculator = Calculator()
    return calculator


@pytest.mark.parametrize(
    'operator, arg1, arg2, expected',
    [
        pytest.param('+', 1, 1, 2),
        pytest.param('-', 1, 1, 0),
        pytest.param('*', 2, 3, 6),
        pytest.param('/', 10, 2, 5),
    ],
)
def test_run_parametrize(operator, arg1, arg2, expected):
    assert Calculator().run(operator, arg1, arg2) == expected


def test_run_not_number(calculator):
    with pytest.raises(NotNumberArgument):
        b = calculator.run('+', 1, 'a')
        assert b is None


def test_run_wrong_operation(calculator):
    with pytest.raises(WrongOperation):
        b = calculator.run('^', 2, 3)
        assert b is None


def test_run_empty_memory1(calculator):
    with pytest.raises(EmptyMemory):
        b = calculator.in_memory()
        assert b is None


def test_run_empty_memory2(calculator):
    with pytest.raises(EmptyMemory):
        b = calculator.run('/', 2)
        assert b is None


def test_run_zero_division(calculator):
    try:
        b = calculator.run('/', 1, 0)
    except CalculatorError as exc:
        assert type(exc.__cause__) == ZeroDivisionError
