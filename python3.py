# 01 - Karakterek száma a fájlban
def karakterek_szama(fname):
    with open(fname, 'r') as f:
        return len(f.read())

# 02 - Szavak száma a fájlban
def szavak_szama(fname):
    with open(fname, 'r') as f:
        return len(f.read().split())

# 03 - Sorok száma a fájlban
def sorok_szama(fname):
    with open(fname, 'r') as f:
        return len(f.readlines())

# 04 - 'r' betűk száma a fájlban
def r_betuk_szama(fname):
    with open(fname, 'r') as f:
        return f.read().count('r')

# 05 - 'lorem' szavak száma a fájlban
def lorem_szavak_szama(fname):
    with open(fname, 'r') as f:
        return f.read().lower().count('lorem')

# 06 - Leggyyakoribb karakter a fájlban
def leggyakoribb_karakter(fname):
    with open(fname, 'r') as f:
        content = f.read()
        from collections import Counter
        return Counter(content).most_common(1)[0][0]

# 07 - Leghosszabb sor hossza a fájlban
def leghosszabb_sor_hossza(fname):
    with open(fname, 'r') as f:
        return max(len(line) for line in f)

# 08 - Téglalap osztály
class Teglalap:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def kerulet(self):
        return 2 * (self.a + self.b)

    def terulet(self):
        return self.a * self.b

# 09 - Négyzet osztály
class Negyzet:
    def __init__(self, a):
        self.a = a

    def kerulet(self):
        return 4 * self.a

    def terulet(self):
        return self.a ** 2

# 10 - Kocka osztály
class Kocka:
    def __init__(self, a):
        self.a = a

    def terfogat(self):
        return self.a ** 3

    def felszin(self):
        return 6 * self.a ** 2

# 11 - String fájlba írása
def string_fajlba(s, fname):
    with open(fname, 'w') as f:
        f.write(s)

# 12 - Számtani sorozat fájlba írása
def szaz_szam_fajlba(fname):
    with open(fname, 'w') as f:
        for i in range(1, 101):
            f.write(f"{i}\n")

# 13 - Első karakter a szövegfájlban
def elso_karakter_a_fajlban(fname):
    with open(fname, 'r') as f:
        return f.read(1)

# 14 - Utolsó karakter a szövegfájlban
def utolso_karakter_a_fajlban(fname):
    with open(fname, 'r') as f:
        content = f.read()
        return content[-1] if content else None

# 15 - Számok összege egy szövegfájlban
def szamok_osszege_a_fajlban(fname):
    with open(fname, 'r') as f:
        numbers = [int(word) for word in f.read().split()]
        return sum(numbers)

# 16 - Számok átlaga egy szövegfájlban
def szamok_atlaga_a_fajlban(fname):
    with open(fname, 'r') as f:
        numbers = [int(word) for word in f.read().split()]
        return sum(numbers) / len(numbers) if numbers else 0

# 17 - Páros számok száma egy szövegfájlban
def paros_szamok_szama_a_fajlban(fname):
    with open(fname, 'r') as f:
        numbers = [int(word) for word in f.read().split()]
        return len([num for num in numbers if num % 2 == 0])

# 18 - Páratlan számok száma egy szövegfájlban
def paratlan_szamok_szama_a_fajlban(fname):
    with open(fname, 'r') as f:
        numbers = [int(word) for word in f.read().split()]
        return len([num for num in numbers if num % 2 != 0])

# 19 - Pozitív számok száma egy szövegfájlban
def pozitiv_szamok_szama_a_fajlban(fname):
    with open(fname, 'r') as f:
        numbers = [int(word) for word in f.read().split()]
        return len([num for num in numbers if num > 0])

# 20 - Negatív számok száma egy szövegfájlban
def negativ_szamok_szama_a_fajlban(fname):
    with open(fname, 'r') as f:
        numbers = [int(word) for word in f.read().split()]
        return len([num for num in numbers if num < 0])

# 21 - Legkisebb szám egy szövegfájlban
def legkisebb_szam_a_fajlban(fname):
    with open(fname, 'r') as f:
        numbers = [int(word) for word in f.read().split()]
        return min(numbers) if numbers else None

# 22 - Legnagyobb szám egy szövegfájlban
def legnagyobb_szam_a_fajlban(fname):
    with open(fname, 'r') as f:
        numbers = [int(word) for word in f.read().split()]
        return max(numbers) if numbers else None

# 23 - Párosok egy szövegfájlból
def parosok_a_fajlbol(fname):
    with open(fname, 'r') as f:
        numbers = [int(word) for word in f.read().split()]
        return [num for num in numbers if num % 2 == 0]

# 24 - Páratlanok egy szövegfájlból
def paratlanok_a_fajlbol(fname):
    with open(fname, 'r') as f:
        numbers = [int(word) for word in f.read().split()]
        return [num for num in numbers if num % 2 != 0]

# 25 - Pozitívok egy szövegfájlból
def pozitiv_a_fajlbol(fname):
    with open(fname, 'r') as f:
        numbers = [int(word) for word in f.read().split()]
        return [num for num in numbers if num > 0]

# 26 - Negatívok egy szövegfájlból
def negativok_a_fajlbol(fname):
    with open(fname, 'r') as f:
        numbers = [int(word) for word in f.read().split()]
        return [num for num in numbers if num < 0]

# 27 - Leggyakoribb szám a szövegfájlban
def leggyakoribb_szam_a_fajlban(fname):
    with open(fname, 'r') as f:
        numbers = [int(word) for word in f.read().split()]
        from collections import Counter
        return Counter(numbers).most_common(1)[0][0] if numbers else None

# 28 - Hárommal osztható számok a szövegfájlban
def harommal_oszthato_szamok_a_fajlban(fname):
    with open(fname, 'r') as f:
        numbers = [int(word) for word in f.read().split()]
        return [num for num in numbers if num % 3 == 0]

# 29 - Néggyel osztható számok a szövegfájlban
def neggyel_oszthato_szamok_a_fajlban(fname):
    with open(fname, 'r') as f:
        numbers = [int(word) for word in f.read().split()]
        return [num for num in numbers if num % 4 == 0]