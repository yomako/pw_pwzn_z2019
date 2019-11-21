"""
Na (1 pkt.):
Napisz program do sprawdzenia poprawności skompresowanego wyjścia poprzedniej
funkcji.
Funkcja MUSI w swej implementacji korzystać z wyrażeń regularnych.

Funkcja na wejściu przyjmuje nazwę pliku do sprawdzenia, na wyjściu zwraca
dwuelementową tuplę zawierającą liczbę poprawnych wierszy:
- na indeksie 0 płeć F
- na indeksie 1 płeć M
"""
import re


def check_animal_list(file_path):
    with open(file_path, 'r') as _file:
        lines = _file.readlines()

    males = 0
    females = 0

    for line in lines:
        if bool(re.fullmatch(r'^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}_M_[\d]\.[\d]{3}e[\-\+][\d]{2}$', line.strip())):
            males += 1
        if bool(re.fullmatch(r'^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}_F_[\d]\.[\d]{3}e[\-\+][\d]{2}$', line.strip())):
            females += 1

    return (females, males)


if __name__ == '__main__':
    assert check_animal_list('s_animals_sce.txt') == (2, 2)
    print(check_animal_list('animals_sc_corrupted.txt'))
    # assert check_animal_list('animals_sc_corrupted.txt') == (6, 0) # czy na pewno tak
