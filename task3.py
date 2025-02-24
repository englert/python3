import json

lista = [
'''
01-------------------------------------------------------------
Feladat: Karakterek száma a fájlban.
A karakterek_szama nevű függvény
paraméterként egy fájlnevet kap és
visszatér a fájlban levő karakterek számával. ('\n karakterekkel együtt')
'''
,
'''
02-------------------------------------------------------------
Feladat: Szavak száma a fájlban
A szavak_szama nevű függvény
paraméterként egy fájlnevet kap és
visszatér a fájlban levő szavak számával.
'''
,
'''
03-------------------------------------------------------------
Feladat: Sorok száma a fájlban.
A sorok_szama nevű függvény
paraméterként egy fájlnevet kap és
visszatér a fájlban levő sorok számával.
'''
,
'''
04-------------------------------------------------------------
Feladat: r betük száma a fájlban.
Az r_betuk_szama nevű függvény
paraméterként egy fájlnevet kap és
visszatér a fájlban levő 'r' betük számával.
'''
,
'''
05.-------------------------------------------------------------
Feladat: lorem szavak száma a fájlban.
A lorem_szavak_szama nevű függvény 
paraméterként egy fájlnevet kap és
visszatér a  fájlban levő "lorem" szavak számával.
'''
,
'''
06-------------------------------------------------------------
Feladat: A leggyakoribb karakter a fájlban.
A leggyakoribb_karakter(fname) függvény
paraméterként egy fájlnevet kap és
visszatér a  fájlban leggyakrabban előforduló karakterrel.
'''
,
'''
07------------------------------------------------------------- 
Feladat: A leghosszabb sor hossza a fájlban.
A leghosszabb_sor_hossza(fname) függvény
paraméterként egy fájlnevet kap és
visszatér a  fájlban levő leghosszabb sor hosszával.
'''
,
'''
08-------------------------------------------------------------
Feladat: Téglalap osztály definiálása. [Objektumorientált programozás]
Hozz létre egy osztályt Teglalap néven.
A Teglalap osztály lehetővé teszi a téglalap oldalhosszúságainak tárolását.
A Teglalap osztály rendelkezik egy kerulet() nevü metódussal, amely az osztály segítségével létrehozott objektum metódusaként visszaadja az adott objektum kerületét.
A Teglalap osztály rendelkezik egy terulet() nevü metódussal, amely az osztály segítségével létrehozott objektum metódusaként visszaadja az adott objektum területét.
'''
,
'''
09-------------------------------------------------------------
Feladat: Négyzet osztály definiálása. [Objektumorientált programozás]
Hozz létre egy osztályt Negyzet néven.
A Negyzet osztály lehetővé teszi a negyzet oldalhosszúságának tárolását.
A Negyzet osztály rendelkezik egy kerulet() nevü metódussal, amely az osztály segítségével létrehozott objektum metódusaként visszaadja az adott objektum kerületét.
A Negyzet osztály rendelkezik egy terulet() nevü metódussal, amely az osztály segítségével létrehozott objektum metódusaként visszaadja az adott objektum területét.
'''
,
'''
10-------------------------------------------------------------
Feladat: Kocka osztály definiálása. [Objektumorientált programozás]
Hozz létre egy osztályt Kocka néven.
A Kocka osztály lehetővé teszi a kocka oldalhosszúságának tárolását.
A Kocka osztály rendelkezik egy tefogat() nevü metódussal, amely az osztály segítségével létrehozott objektum metódusaként visszaadja az adott objektum térfogatát.
A Kocka osztály rendelkezik egy felszin() nevü metódussal, amely az osztály segítségével létrehozott objektum metódusaként visszaadja az adott objektum felszínét.
'''
,
'''
11-------------------------------------------------------------
Feladat: String fájlba írása
Készíts függvényt string_fajlba néven, amely az első paraméterként kapott sztringet fájlba írja.
A fájl nevét második paraméterként kapja meg a függvény.
'''
,
'''
12-------------------------------------------------------------
Feladat: Számtani sorozat fájlba írása
Készíts függvényt szaz_szam_fajlba néven, amely 1-tól 100-ig egyesével kiírja a számokat egy fájlba.
Minden szám kerüljön új sorba.
A fájl nevét paraméterként kapja meg a függvény.
'''
,
'''
13 --------------------------------------------------------------------------------------------
Feladat: Első karakter a szövegfájlban
Írj egy függvényt elso_karakter_a_fajlban néven, amely visszatér egy szövegfájl első karakterével.
A függvény bemenő paramétere a fájl neve.
'''
,
'''
14--------------------------------------------------------------------------------------------
Feladat: Utolsó karakter a szövegfájlban
Írj egy függvényt utolso_karakter_a_fajlban néven, amely visszatér egy szövegfájl utolsó karakterével.
A függvény bemenő paramétere a fájl neve.
'''
,
'''
15--------------------------------------------------------------------------------------------
Feladat: Számok összege egy szövegfájlban.
Írj egy függvényt szamok_osszege_a_fajlban néven amely visszatér egy szövegfájlban levő számok összegével.
A függvény bemenő paramétere a fájl neve.
'''
,
'''
16--------------------------------------------------------------------------------------------
Feladat: Számok átlaga egy szövegfájlban.
Írj egy függvényt szamok_atlaga_a_fajlban néven, amely visszatér egy szövegfájlban levő számok átlagával.
A függvény bemenő paramétere a fájl neve.
'''
,
'''
17--------------------------------------------------------------------------------------------
Feladat: Páros számok száma egy szövegfájlban.
Írj egy függvényt paros_szamok_szama_a_fajlban néven, amely visszatér egy szövegfájlban levő páros számok számával.
A függvény bemenő paramétere a fájl neve.
'''
,
'''
18--------------------------------------------------------------------------------------------
Feladat: Páratlan számok száma egy szövegfájlban.
Írj egy függvényt paratlan_szamok_szama_a_fajlban néven, amely visszatér egy szövegfájlban levő páratlan számok számával.
A függvény bemenő paramétere a fájl neve.
'''
,
'''
19--------------------------------------------------------------------------------------------
Feladat: Pozitív számok száma egy szövegfájlban.
Írj egy függvényt pozitiv_szamok_szama_a_fajlban néven, amely visszatér egy szövegfájlban levő pozitiv számok számával.
A függvény bemenő paramétere a fájl neve.
'''
,
'''
20--------------------------------------------------------------------------------------------
Feladat: Negatív számok száma egy szövegfájlban.
Írj egy függvényt negativ_szamok_szama_a_fajlban néven, amely visszatér egy szövegfájlban levő negativ számok számával.
A függvény bemenő paramétere a fájl neve.
'''
,
'''
21--------------------------------------------------------------------------------------------
Feladat: Legkisebb szám egy szövegfájlban.
Írj egy függvényt legkisebb_szam_a_fajlban néven, amely visszatér egy szövegfájlban levő lekisebb számmal.
A függvény bemenő paramétere a fájl neve.
'''
,
'''
22--------------------------------------------------------------------------------------------
Feladat: Legnagyobb szám egy szövegfájlban.
Írj egy függvényt legnagyobb_szam_a_fajlban néven, amely visszatér egy szövegfájlban levő legnagyobb számmal.
A függvény bemenő paramétere a fájl neve.
'''
,
'''
23--------------------------------------------------------------------------------------------
Feladat: Párosok egy szövegfájlból.
Írj egy függvényt parosok_a_fajlbol néven, amely visszatér a szövegfájlban levő páros számokkal mint listával.
A függvény bemenő paramétere a fájl neve.
'''
,
'''
24--------------------------------------------------------------------------------------------
Feladat: Páratlanok egy szövegfájlból.
Írj egy függvényt paratlanok_a_fajlbol néven, amely visszatér a szövegfájlban levő páratlan számokkal mint listával.
A függvény bemenő paramétere a fájl neve.
'''
,
'''
25--------------------------------------------------------------------------------------------
Feladat: Pozitívok egy szövegfájlból.
Írj egy függvényt pozitiv_a_fajlbol néven, amely visszatér a szövegfájlban levő pozitiv számokkal mint listával.
A függvény bemenő paramétere a fájl neve.
'''
,
'''
26--------------------------------------------------------------------------------------------
Feladat: Negatívok egy szövegfájlból.
Írj egy függvényt negativok_a_fajlbol néven, amely visszatér a szövegfájlban levő negativ számokkal mint listával.
A függvény bemenő paramétere a fájl neve.
'''
,
'''
27--------------------------------------------------------------------------------------------
Feladat: Leggyakoribb szám a szövegfájlban.
Írj egy függvényt leggyakoribb_szam_a_fajlban néven, amely visszatér a szövegfájlban levő leggyakoribb számmal.
A függvény bemenő paramétere a fájl neve.
'''
,
'''
28--------------------------------------------------------------------------------------------
Feladat: Hárommal osztható számok a szövegfájlban.
Írj egy függvényt harommal_oszthato_szamok_a_fajlban néven, amely visszatér a szövegfájlban levő hárommal osztható számok listájával.
A függvény bemenő paramétere a fájl neve.
'''
,
'''
29--------------------------------------------------------------------------------------------
Feladat: Neggyel osztható számok a szövegfájlban.
A neggyel_oszthato_szamok_a_fajlban függvény
egy függvényt neggyel_oszthato_szamok_a_fajlban néven, amely visszatér a szövegfájlban levő neggyel osztható számok listájával.
A függvény bemenő paramétere a fájl neve.
'''
]

with open('task3.json','w', encoding='utf-8') as f:
    f.write(json.dumps(lista))

