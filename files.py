# Python, dosyalar oluşturma, okuma, güncelleme ve silme işlemleri için fonksiyonlara sahiptir.

# Bir dosyayı açma
dosyam = open('dosyam.txt', 'w')

# Bazı bilgileri al
print('Ad: ', dosyam.name)
print('Kapalı mı: ', dosyam.closed)
print('Açılış Modu: ', dosyam.mode)

# Dosyaya yazma
dosyam.write('Python\'ı seviyorum')
dosyam.write(' ve JavaScript')
dosyam.close()

# Dosyaya ekleme (append)
dosyam = open('dosyam.txt', 'a')
dosyam.write(' Ayrıca PHP\'yi de seviyorum')
dosyam.close()

# Dosyadan okuma
dosyam = open('dosyam.txt', 'r+')
metin = dosyam.read(100)
print(metin)
