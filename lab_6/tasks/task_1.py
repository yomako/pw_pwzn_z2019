"""
Jesteś informatykiem w firmie Noe's Animals Redistribution Center.
Firma ta zajmuje się międzykontynentalnym przewozem zwierząt.
---------
Celem zadania jest przygotowanie funkcji pozwalającej na przetworzenie
pliku wejściowego zawierającego listę zwierząt do trasnportu.
Funkcja ma na celu wybranie par (samiec i samica) z każdego gatunku,
tak by łączny ładunek był jak najlżeszy (najmniejsza masa osobnika
rozpatrywana jest względem gatunku i płci).
---------
Na 1 pkt.
Funkcja ma tworzyć plik wyjściowy zwierający listę wybranych zwierząt
w formacie wejścia (takim samym jak w pliku wejściowym).
Wyjście ma być posortowane alfabetycznie względem gatunku,
a następnie względem nazwy zwierzęcia.
---------
Na +1 pkt.
Funkcja ma opcję zmiany formatu wejścia na:
"<id>_<gender>_<mass>"
(paramter "compressed") gdzie:
- "id" jest kodem zwierzęcia (uuid),
- "gender" to jedna litera (F/M)
- "mass" zapisana jest w kilogramach w notacji wykładniczej
z dokładnością do trzech miejsc po przecinku np. osobnik ważący 456 gramów
ma mieć masę zapisaną w postaci "4.560e-01"
---------
Na +1 pkt.
* Ilość pamięci zajmowanej przez program musi być stałą względem
liczby zwierząt.
* Ilość pamięci może rosnąć liniowo z ilością gatunków.
---------
UWAGA: Możliwe jest wykonanie tylko jednej opcji +1 pkt.
Otrzymuje się wtedy 2 pkt.
UWAGA 2: Wszystkie jednoski masy występują w przykładzie.
"""
from pathlib import Path
import csv
from decimal import Decimal


def select_animals(input_path, output_path, compressed=False):
    output = []
    header = None
    with open(input_path, 'r') as _file:
        reader = csv.reader(_file, delimiter=',')
        header = next(reader, None)
        dictreader = csv.DictReader(_file, delimiter=',', fieldnames=header)
        notation = {'g': 1e-3, 'mg': 1e-6, 'kg': 1, 'Mg': 1e3}
        genuses = set()

        for row in dictreader:
            genuses.add(row['genus'])

        for genus in genuses:
            for gender in ['male', 'female']:
                _file.seek(0)
                probe = []
                masses = []
                for row in dictreader:
                    if row['gender'] == gender and row['genus'] == genus:
                        probe.append(row)
                        splited_mass = row['mass'].split(' ')
                        masses.append(float(splited_mass[0]) * notation[splited_mass[1]])

                output.append([x for _, x in sorted(zip(masses, probe))][0])

        output = sorted(output, key=lambda i: (i['genus'], i['name']))

    with open(output_path, 'w') as _file:
        if compressed:
            writer = csv.writer(_file, delimiter=',', quotechar="*")
            writer.writerow(['uuid_gender_mass'])
            short_gender = {'male': 'M', 'female': 'F'}
            for o in output:
                splited_mass = o['mass'].split(' ')
                writer.writerow(['{}_{}_{}'.format(o['id'], short_gender[o['gender']], '%.3e' % Decimal(float(splited_mass[0]) * notation[splited_mass[1]]))])
        else:
            writer = csv.DictWriter(_file, fieldnames=header)
            writer.writeheader()
            writer.writerows(output)


if __name__ == '__main__':
    input_path = Path('s_animals.txt')
    output_path = Path('s_animals_s.txt')
    select_animals(input_path, output_path)
    with open(output_path) as generated:
        with open('s_animals_se.txt') as expected:
            assert generated.read() == expected.read()

    output_path = Path('s_animals_sc.txt')
    select_animals(input_path, output_path, True)
    with open(output_path) as generated:
        with open('s_animals_sce.txt') as expected:
            assert generated.read() == expected.read()
