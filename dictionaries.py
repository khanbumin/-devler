# Bir Sözlük (Dictionary), sırasız, değiştirilebilir ve endekslenmiş bir koleksiyondur. Tekrarlayan üyeler içermez.

# Sözlük oluşturma
kisi = {
    'ad': 'Ahmet',
    'soyad': 'Yılmaz',
    'yas': 30
}

# İnşa ediciyi kullanma
# kisi2 = dict(ad='Ayşe', soyad='Kara')

# Değer al
print(kisi['ad'])
print(kisi.get('soyad'))

# Anahtar/değer ekleme
kisi['telefon'] = '588-595-5999'

# Sözlük anahtarlarını al
print(kisi.keys())

# Sözlük öğelerini al
print(kisi.items())

# Sözlüğü kopyala
kisi2 = kisi.copy()
kisi2['şehir'] = 'İstanbul'

# Öğe silme
del(kisi['yas'])
kisi.pop('telefon')

# Temizleme
kisi.clear()

# Uzunluğu al
print(len(kisi2))

# Sözlük listesi
kisiler = [
    {'ad': 'Merve', 'yas': 30},
    {'ad': 'Emre', 'yas': 25}
]

print(kisiler[1]['ad'])
