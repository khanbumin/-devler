# Bir Tuple (Demet), sıralı ve değiştirilemez bir koleksiyondur. Tekrarlayan üyelere izin verir.

# Tuple oluşturma
meyveler = ('Elma', 'Portakal', 'Üzüm')

# Bir oluşturucu kullanma
# meyveler2 = tuple(('Elma', 'Portakal', 'Üzüm'))

# Tek bir değer kullanacaksanız sona virgül eklenmelidir
meyveler2 = ('Elma',)

# Değeri alma
print(meyveler[1])

# Değiştirilemez (Immutable), değeri değiştiremezsiniz
# meyveler[0] = 'Armut'

# Demeti silme
del meyveler2

# Uzunluğu alma
print(len(meyveler))


# Bir Set (Küme), sırasız ve dizinlenmemiş bir koleksiyondur. Tekrarlayan üyelere izin vermez.

# Set oluşturma
meyve_kumesi = {'Elma', 'Portakal', 'Mango'}

# Set içinde bulunup bulunmadığını kontrol etme
print('Elma' in meyve_kumesi)

# Kümeye ekleme
meyve_kumesi.add('Üzüm')

# Kümeden kaldırma
meyve_kumesi.remove('Üzüm')

# Tekrarlayıcı ekleme
meyve_kumesi.add('Elma')

# Küme temizleme
meyve_kumesi.clear()

# Silme
del meyve_kumesi

# meyve_kumesi artık tanımlanmış değil
# print(meyve_kumesi)
