import os
import pytest
import math
import random
import json
from unittest.mock import patch


if not os.path.exists('python3.py'):
    with open('task3.json') as json_data:
        lista = json.load(json_data)
    
    random.shuffle(lista)
    text = "'''\n\n\n\n#--------------------------\n'''".join(lista)
    
    with open('python3.py', 'w') as f:
        f.write("#--------------------------\n'''")
        f.writelines(text)
        f.write("'''\n\n\n\n#=====================================")
        

from python3 import *

# 01 - Karakterek száma a fájlban
def test_karakterek_szama():
    assert karakterek_szama('lorem.txt') == 18047
    assert karakterek_szama('lorem2.txt') == 37943

# 02 - Szavak száma a fájlban
def test_szavak_szama():
    assert szavak_szama('lorem.txt') == 2304
    assert szavak_szama('lorem2.txt') == 5010

# 03 - Sorok száma a fájlban
def test_sorok_szama():
    assert sorok_szama('lorem.txt') == 82
    assert sorok_szama('lorem2.txt') == 167

# 04 - 'r' betűk száma a fájlban
def test_r_betuk_szama():
    assert r_betuk_szama('lorem.txt') == 790  
    assert r_betuk_szama('lorem2.txt') == 1703 

# 05 - 'lorem' szavak száma a fájlban
def test_lorem_szavak_szama():
    assert lorem_szavak_szama('lorem.txt') == 28 
    assert lorem_szavak_szama('lorem2.txt') == 54

# 06 - Leggyyakoribb karakter a fájlban
def test_leggyakoribb_karakter():
    assert leggyakoribb_karakter('lorem.txt') == 'i' 
    assert leggyakoribb_karakter('lorem2.txt') == 'x' 

# 07 - Leghosszabb sor hossza a fájlban
def test_leghosszabb_sor_hossza():
    assert leghosszabb_sor_hossza('lorem.txt') == 304  
    assert leghosszabb_sor_hossza('lorem2.txt') == 264
    
# 08 - Téglalap osztály
def test_teglalap():
    t = Teglalap(3, 4)
    assert t.kerulet() == 14
    assert t.terulet() == 12
    t2 = Teglalap(5, 9)
    assert t2.kerulet() == 28
    assert t2.terulet() == 45

# 09 - Négyzet osztály
def test_negyzet():
    n = Negyzet(5)
    assert n.kerulet() == 20
    assert n.terulet() == 25
    n2 = Negyzet(6)
    assert n2.kerulet() == 24
    assert n2.terulet() == 36

# 10 - Kocka osztály
def test_kocka():
    k = Kocka(3)
    assert k.terfogat() == 27
    assert k.felszin() == 54
    k2 = Kocka(3)
    assert k2.terfogat() == 27
    assert k2.felszin() == 54

# 11 - String fájlba írása
def test_string_fajlba():
    string_fajlba("Hello World!", 'test_file.txt')
    with open('test_file.txt', 'r') as f:
        assert f.read() == "Hello World!"
    os.remove('test_file.txt')

# 12 - Számtani sorozat fájlba írása
def test_szaz_szam_fajlba():
    szaz_szam_fajlba('test_file.txt')
    with open('test_file.txt', 'r') as f:
        lines = f.readlines()
        assert len(lines) == 100
        assert lines[0].strip() == "1"
        assert lines[99].strip() == "100"
    os.remove('test_file.txt')

# 13 - Első karakter a szövegfájlban
def test_elso_karakter_a_fajlban():
    with open('test_file.txt', 'w') as f:
        f.write("Hello World!")
    assert elso_karakter_a_fajlban('test_file.txt') == "H"
    os.remove('test_file.txt')

# 14 - Utolsó karakter a szövegfájlban
def test_utolso_karakter_a_fajlban():
    with open('test_file.txt', 'w') as f:
        f.write("Hello World!")
    assert utolso_karakter_a_fajlban('test_file.txt') == "!"
    os.remove('test_file.txt')


# 15 - Számok összege egy szövegfájlban
def test_szamok_osszege_a_fajlban():
    assert szamok_osszege_a_fajlban('szamok1.txt') == 16
    assert szamok_osszege_a_fajlban('szamok2.txt') == 100

# 16 - Számok átlaga egy szövegfájlban
def test_szamok_atlaga_a_fajlban():
    assert szamok_atlaga_a_fajlban('szamok1.txt') ==  1.0
    assert szamok_atlaga_a_fajlban('szamok2.txt') ==  4.166666666666667

# 17 - Páros számok száma egy szövegfájlban
def test_paros_szamok_szama_a_fajlban():
    assert paros_szamok_szama_a_fajlban('szamok1.txt') == 10
    assert paros_szamok_szama_a_fajlban('szamok2.txt') == 14

# 18 - Páratlan számok száma egy szövegfájlban
def test_paratlan_szamok_szama_a_fajlban():
    assert paratlan_szamok_szama_a_fajlban('szamok1.txt') == 6
    assert paratlan_szamok_szama_a_fajlban('szamok2.txt') == 10

# 19 - Pozitív számok száma egy szövegfájlban
def test_pozitiv_szamok_szama_a_fajlban():
    assert pozitiv_szamok_szama_a_fajlban('szamok1.txt') == 10
    assert pozitiv_szamok_szama_a_fajlban('szamok2.txt') == 14
    
# 20 - Negatív számok száma egy szövegfájlban
def test_negativ_szamok_szama_a_fajlban():
    assert negativ_szamok_szama_a_fajlban('szamok1.txt') == 4 
    assert negativ_szamok_szama_a_fajlban('szamok2.txt') == 8

# 21 - Legkisebb szám egy szövegfájlban
def test_legkisebb_szam_a_fajlban():
    assert legkisebb_szam_a_fajlban('szamok1.txt') == -6  
    assert legkisebb_szam_a_fajlban('szamok2.txt') == -45  

# 22 - Legnagyobb szám egy szövegfájlban
def test_legnagyobb_szam_a_fajlban():
    assert legnagyobb_szam_a_fajlban('szamok1.txt') == 4  
    assert legnagyobb_szam_a_fajlban('szamok2.txt') == 66 

# 23 - Párosok egy szövegfájlból
def test_parosok_a_fajlbol():
    assert parosok_a_fajlbol('szamok1.txt') == [4, 2, 4, 2, 0, -4, -6, 0, 4, 4]
    assert parosok_a_fajlbol('szamok2.txt') == [4, 2, 4, 2, 0, -4, -6, 0, 4, 4, 12, 44, 66, -2]

# 24 - Páratlanok egy szövegfájlból
def test_paratlanok_a_fajlbol():
    assert paratlanok_a_fajlbol('szamok1.txt') == [3, 1, 3, 1, -1, -1]
    assert paratlanok_a_fajlbol('szamok2.txt') == [3, 1, 3, 1, -1, -1, 13, -45, -1, -3]

# 25 - Pozitívok egy szövegfájlból
def test_pozitiv_a_fajlbol():
    assert pozitiv_a_fajlbol('szamok1.txt') == [4, 3, 2, 1, 4, 3, 2, 1, 4, 4] 
    assert pozitiv_a_fajlbol('szamok2.txt') == [4, 3, 2, 1, 4, 3, 2, 1, 4, 4, 12, 13, 44, 66]

# 26 - Negatívok egy szövegfájlból
def test_negativok_a_fajlbol():
    assert negativok_a_fajlbol('szamok1.txt') == [-1, -1, -4, -6] 
    assert negativok_a_fajlbol('szamok2.txt') == [-1, -1, -4, -6, -45, -1, -2, -3]

# 27 - Leggyakoribb szám a szövegfájlban
def test_leggyakoribb_szam_a_fajlban():
    assert leggyakoribb_szam_a_fajlban('szamok1.txt') == 4 
    assert leggyakoribb_szam_a_fajlban('szamok2.txt') == 4 

# 28 - Hárommal osztható számok a szövegfájlban
def test_harommal_oszthato_szamok_a_fajlban():
    assert harommal_oszthato_szamok_a_fajlban('szamok1.txt') == [3, 3, 0, -6, 0] 
    assert harommal_oszthato_szamok_a_fajlban('szamok2.txt') ==  [3, 3, 0, -6, 0, 12, -45, 66, -3]

# 29 - Néggyel osztható számok a szövegfájlban
def test_neggyel_oszthato_szamok_a_fajlban():
    assert neggyel_oszthato_szamok_a_fajlban('szamok1.txt') == [4, 4, 0, -4, 0, 4, 4]
    assert neggyel_oszthato_szamok_a_fajlban('szamok2.txt') == [4, 4, 0, -4, 0, 4, 4, 12, 44] 
