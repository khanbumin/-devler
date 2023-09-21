# Bir işlev (fonksiyon), yalnızca çağrıldığında çalışan bir kod bloğudur. Python'da süslü parantezler yerine girinti (boşluk veya sekme) kullanırız.

# İşlev oluşturma
def selamVer(isim='Mehmet'):
    print(f'Merhaba {isim}')


# Değer döndürme
def toplamAl(sayi1, sayi2):
    toplam = sayi1 + sayi2
    return toplam


# Bir lambda işlevi, küçük, anonim bir işlevdir.
# Bir lambda işlevi, herhangi bir sayıda argüman alabilir, ancak yalnızca bir ifadeye sahip olabilir. JS ok işlevlerine çok benzerdir.

toplamAl = lambda sayi1, sayi2: sayi1 + sayi2

print(toplamAl(10, 3))
