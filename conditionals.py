# If/Else koşulları, bir şeyin doğru veya yanlış olmasına bağlı olarak bir şey yapmayı kararlaştırmak için kullanılır.

x = 21
y = 20

# Karşılaştırma Operatörleri (==, !=, >, <, >=, <=) - Değerleri karşılaştırmak için kullanılır

# Basit bir if
if x > y:
  print(f'{x} {y}\'dan büyüktür')

# If/else
if x > y:
  print(f'{x} {y}\'dan büyüktür')
else:
  print(f'{y} {x}\'dan büyüktür')

# elif
if x > y:
  print(f'{x} {y}\'dan büyüktür')
elif x == y:
  print(f'{x} {y}\'e eşittir')
else:
  print(f'{y} {x}\'dan büyüktür')

# İç içe geçmiş if
if x > 2:
  if x <= 10:
    print(f"{x} 2\'den büyük ve 10'a küçüktür")

# Mantıksal operatörler (and, or, not) - Koşullu ifadeleri birleştirmek için kullanılır

# and
if x > 2 and x <= 10:
    print(f"{x} 2\'den büyük ve 10'a küçüktür")

# or
if x > 2 or x <= 10:
    print(f"{x} 2'den büyük veya 10'a küçüktür")

# not
if not(x == y):
  print(f'{x} {y}\'e eşit değildir')

# Üyelik Operatörleri (in, not in) - Üyelik operatörleri, bir dizinin bir nesnede olup olmadığını test etmek için kullanılır

sayilar = [1,2,3,4,5]

# in
if x in sayilar:
  print(x, "sayılar dizisinde bulunur")

# not in
if x not in sayilar:
  print(x, "sayılar dizisinde bulunmaz")

# Kimlik Operatörleri (is, is not) - Nesneleri karşılaştırır, eşit olup olmadıklarını değil, aslında aynı nesne olup olmadıklarını, aynı bellek konumuna sahip olup olmadıklarını karşılaştırır

# is
if x is y:
  print(x, y, 'eşittir')

# is not
if x is not y:
  print(x, y, 'eşit değildir')
