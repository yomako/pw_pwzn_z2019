def count_letters(msg):
    """
    Zwraca pare (znak, liczba zliczeń) dla najczęściej występującego znaku w wiadomości.
    W przypadku równości zliczeń wartości sortowane są alfabetycznie.

    :param msg: Message to count chars in.
    :type msg: str
    :return: Most frequent pair char - count in message.
    :rtype: list
    """
    chars = []
    chars_dict = {}
    for c in msg:
        if c not in chars:
            chars_dict[c] = 1
            chars.append(c)
        else:
            chars_dict[c] += 1

    result = []
    for key in chars_dict.keys():
        if chars_dict[key] == max(chars_dict.values()):
            result.append(key)

    return sorted(result)[0], max(chars_dict.values())

if __name__ == '__main__':
    msg = 'Abrakadabra'
    assert count_letters(msg) == ('a', 4)
    assert count_letters('za') == ('a', 1)