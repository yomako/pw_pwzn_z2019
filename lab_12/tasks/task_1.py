def generate_fibonacci(n=100):
    if n < 1 or n > 100:
        raise RuntimeError
    f_i = 0
    f_ip1 = 1
    for i in range(n):
        yield f_i
        f_ip1, f_i = f_ip1 + f_i, f_ip1


if __name__ == '__main__':
    assert list(generate_fibonacci(1)) == [0]
    assert list(generate_fibonacci(2)) == [0, 1]
    assert sum(generate_fibonacci(10)) == 88
    ii = 0
    for ii in generate_fibonacci():
        pass
    assert ii == 218922995834555169026
    try:
        generate_fibonacci(0)
    except Exception as exc:
        assert isinstance(exc, RuntimeError)
