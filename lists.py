# Bir Liste, sıralı ve değiştirilebilir bir koleksiyondur. Tekrarlayan üyelere izin verir.

# Liste oluşturma
sayilar = [1, 2, 3, 4, 5]
meyveler = ['Elma', 'Portakal', 'Üzüm', 'Armut']

# Bir oluşturucu kullanma
# sayilar2 = list((1, 2, 3, 4, 5))

# Değer al
print(meyveler[1])

# Son değeri al
print(meyveler[-1])

# Uzunluğu al
print(len(meyveler))

# Listeye ekleme
meyveler.append('Mango')

# Listeden kaldırma
meyveler.remove('Üzüm')

# Belirli bir pozisyona ekleme
meyveler.insert(2, 'Çilek')

# Değeri değiştirme
meyveler[0] = 'Yaban Mersini'

# pop ile kaldırma
meyveler.pop(2)

# Listeyi ters çevirme
meyveler.reverse()

# Liste sıralama
meyveler.sort()

# Ters sıralama
meyveler.sort(reverse=True)

print(meyveler)
