import random
import math
import time
from datetime import datetime
from datetime import date
import keyword


# Zdanie 1

# a
# num = random.randint(1, 22)
# print('Szczęśliwy numerek:',{num})

# b
# ru = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
# sr = random.choice(ru)
# print(sr)

# c

# Zdanie 2

# w1 = math.sqrt(2) + math.sqrt(3) + math.sqrt(6)
# w1 = math.floor(w1)
# w1 = math.ceil(w1)
# print(math.sqrt(2))
# print(math.sqrt(3))
# print(math.sqrt(6))
# print(w1)

# w2 = math.sqrt(-5)
# print(w2)


# Zdanie 3

# sek = int(input("Podaj liczbe sekond: "))
# def sekundnik(n):
#     while czas > 0:
#         print(f'Pozostalo {czas} sek.')
#         time.sleep(1)
#         czas -= 1
#
# def sec_rec(czas):
#     print(czas)
#     time.sleep(1)
#     if czas: sec_rec(-1)
#
# sec_rec()


# Zdanie 4

# dzis = datetime.today()
# zajecia = datetime(2024, 11, 19)
# kolokwium = datetime(2025, 1, 7)
#
# dni_od_laboratorium = dzis - zajecia
# dni_do_kolokwium = kolokwium - dzis
#
# print("Zostało do kolokwium: ", dni_do_kolokwium.days)


# Zdanie 5

# slowa = ["for", "print", "break", "done", "bad"]
# for slowo in slowa:
#     if keyword.iskeyword(slowo):
#         print(f"'{slowo}' jest słowem kluczowym.")
#     else:
#         print(f"'{slowo}' NIE jest słowem kluczowym.")


# Zdanie 6

# print("Funkcje w module 'math':")
# print([func for func in dir(math) if callable(getattr(math, func))])

# print("\nFunkcje w 'tuple' nie istnieją, ponieważ to typ danych.")

# print("\nFunkcje w module 'keyword':")
# print([func for func in dir(keyword) if callable(getattr(keyword, func))])


# Zdanie 7

# PI = 3.14159

# def obwod_kola(promien):
#     return 2 * PI * promien

# def pole_kola(promien):
#     return PI * promien**2


# Zdanie 10

# min_val = int(input("Podaj minimalną wartość zakresu: "))
# max_val = int(input("Podaj maksymalną wartość zakresu: "))

# krotka = tuple(random.randint(min_val, max_val) for _ in range(10))
# print(f"Wygenerowana krotka: {krotka}")

# iloczyn = math.prod(krotka)
# srednia_geometryczna = iloczyn**(1/len(krotka))

# print(f"Średnia geometryczna krotki: {srednia_geometryczna}")


# Zdanie 11

# def zgadywanie_liczby():
#     zakres_min = input("Podaj minimalny zakres: ")
#     zakres_max = input("Podaj maksymalny zakres: ")

#     if not zakres_min.isdigit() or not zakres_max.isdigit():
#         print("Zakres musi być liczbami.")
#         return

#     zakres_min = int(zakres_min)
#     zakres_max = int(zakres_max)

#     if zakres_min >= zakres_max:
#         print("Zakres minimalny musi być mniejszy niż maksymalny.")
#         return

#     liczba_do_zgadniecia = random.randint(zakres_min, zakres_max)
#     proby = 3

#     while proby > 0:
#         proba = input("Zgadnij liczbę: ")

#         if not proba.isdigit():
#             print("Podaj poprawną liczbę.")
#             continue

#         proba = int(proba)

#         if proba < liczba_do_zgadniecia:
#             print("Za mało.")
#         elif proba > liczba_do_zgadniecia:
#             print("Za dużo.")
#         else:
#             print("Gratulacje, zgadłeś!")
#             return

#         proby -= 1

#     print(f"Niestety, liczba to {liczba_do_zgadniecia}. Spróbuj ponownie.")

# zgadywanie_liczby()


# Zdanie 12

# def pole_trojkata(bok1, bok2, kat):
#     if not (0 < kat < 90):
#         print("Kąt musi być ostry (0-90 stopni).")
#         return

#     # Sprawdzenie
#     if (bok1 + bok2 <= 0):
#         print("Trójkąt o takich bokach nie istnieje.")
#         return

#     kat_rad = math.radians(kat)
#     pole = 0.5 * bok1 * bok2 * math.sin(kat_rad)
#     print(f"Pole trójkąta wynosi: {pole} jednostek kwadratowych")

# pole_trojkata(5, 7, 30)


# Zdanie 13

# def operacje_na_datach(rok, miesiac, dzien):
#     data = datetime.date(rok, miesiac, dzien)

#     dzien_roku = data.timetuple().tm_yday
#     print(f"Dzień roku: {dzien_roku}")

#     numer_tygodnia = data.isocalendar()[1]
#     print(f"Numer tygodnia: {numer_tygodnia}")
    
#     dwa_tygodnie_przed = data - datetime.timedelta(weeks=2)
#     dwa_tygodnie_po = data + datetime.timedelta(weeks=2)
#     print(f"Data na 2 tygodnie przed: {dwa_tygodnie_przed}")
#     print(f"Data na 2 tygodnie po: {dwa_tygodnie_po}")

#     najblizsza_niedziela = data + datetime.timedelta(days=(6 - data.weekday()))
#     print(f"Najbliższa niedziela: {najblizsza_niedziela}")

#     czas_unixowy = int(data.strftime("%s"))
#     print(f"Czas unixowy: {czas_unixowy}")

# operacje_na_datach(2024, 12, 6)
