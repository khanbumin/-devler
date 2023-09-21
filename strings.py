isim = 'Ahmet'
yas = 37

# Birleştirme (Concatenate)
print('Merhaba, benim adım ' + isim + ' ve ben ' + str(yas) + ' yaşındayım.')

# Dize Biçimlendirme

# Konum belirterek argümanlar
print('Benim adım {isim} ve ben {yas}'.format(isim=isim, yas=yas))

# F-Dizeleri (3.6+)
print(f'Merhaba, benim adım {isim} ve ben {yas} yaşındayım.')

# Dize Metodları

metin = 'merhabadunya'

# İlk harfi büyük yapma
print(metin.capitalize())

# Tüm harfleri büyük yapma
print(metin.upper())

# Tüm harfleri küçük yapma
print(metin.lower())

# Harf büyüklüğünü tersine çevirme
print(metin.swapcase())

# Uzunluğu alma
print(len(metin))

# Değiştirme
print(metin.replace('dunya', 'herkese'))

# Sayma
alt_dizi = 'a'
print(metin.count(alt_dizi))

# İle başlıyor mu
print(metin.startswith('merhaba'))

# İle bitiyor mu
print(metin.endswith('a'))

# Bir listeye bölmek
print(metin.split())

# Pozisyonu bulma
print(metin.find('r'))

# Tümü alfasayısal mı
print(metin.isalnum())

# Tümü alfabetsel mi
print(metin.isalpha())

# Tümü sayısal mı
print(metin.isnumeric())
