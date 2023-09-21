# Bir for döngüsü, bir dizi (liste, tuple, sözlük, küme veya bir dize) üzerinde yineleme yapmak için kullanılır.

kisiler = ['Ali', 'Ayşe', 'Mehmet', 'Zeynep']

# Basit bir for döngüsü
for kisi in kisiler:
  print(f'Geçerli Kişi: {kisi}')

# Break (Döngüyü Kırma)
for kisi in kisiler:
  if kisi == 'Mehmet':
    break
  print(f'Geçerli Kişi: {kisi}')

# Continue (Devam Et)
for kisi in kisiler:
  if kisi == 'Mehmet':
    continue
  print(f'Geçerli Kişi: {kisi}')

# range
for i in range(len(kisiler)):
  print(kisiler[i])

for i in range(0, 11):
  print(f'Sayı: {i}')

# While döngüleri, bir koşul doğru olduğu sürece belirli bir dizi ifadeyi çalıştırır.

sayac = 0
while sayac < 10:
  print(f'Sayac: {sayac}')
  sayac += 1
