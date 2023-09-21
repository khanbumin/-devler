'''
Bu bir
çok satırlı yorumdur
veya belge dizisi (bir işlemin amacını tanımlamak için kullanılır)
tek veya çift tırnaklarla olabilir
'''

"""
DEĞİŞKEN KURALLARI:
  - Değişken adları büyük-küçük harfe duyarlıdır (isim ve ISIM farklı değişkenlerdir)
  - Bir harf veya alt çizgi ile başlamalıdır
  - Sayılar içerebilir, ancak bir rakamla başlayamazlar
"""

# x = 1           # tamsayı (int)
# y = 2.5         # ondalık sayı (float)
# isim = 'ahmet'   # dize (str)
# havalı_mı = True  # mantıksal (bool)

# Birden çok değişken atama
x, y, isim, havalı_mı = (1, 2.5, 'Ahmet', True)

# Temel matematik işlemleri
a = x + y

# Tür dönüşümü (Casting)
x = str(x)
y = int(y)
z = float(y)

print(type(z), z)
