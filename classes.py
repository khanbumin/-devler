
# Bir sınıf, nesneleri oluşturmak için bir şablondur. Bir nesnenin ilişkilendirilmiş özellikleri ve metotları (fonksiyonları) vardır. Python'da neredeyse her şey bir nesnedir.

# Sınıf oluşturma
class Kullanici:

  # Yapıcı (Constructor) metodu
  def __init__(self, ad, soyad, email, yas):
    self.ad = ad
    self.soyad = soyad
    self.email = email
    self.yas = yas
    
    # Değişkenlerin kapsülleme (encapsulation) eklenmesi... Kapsülleme, değişkenleri erişilemez veya sınırlı bir şekilde alt sınıflardan erişilebilir hale getirme kavramıdır.
    self._ozel = 1000 # Kapsülleme ile korunan değişkenler, yapıcı içinde '_' ile tanımlanır.

  def selam(self):
      return f'Adım {self.ad} {self.soyad} ve yaşım {self.yas}'

  def dogum_gunu(self):
      self.yas += 1
 
 # Kapsülleme değişkeni için bir fonksiyon
  def kapsul_degerini_yazdir(self):
      print(self._ozel)

# Sınıfı genişletme (inheritance)
class Musteri(Kullanici):
  # Yapıcı (Constructor) metodu
  def __init__(self, ad, soyad, email, yas):
      Kullanici.__init__(self, ad, soyad, email, yas) # Doğru üst sınıf yapıcısını çağırmak için
      self.ad = ad
      self.soyad = soyad
      self.email = email
      self.yas = yas
      self.bakiye = 0

  def bakiye_ayarla(self, bakiye):
      self.bakiye = bakiye

  def selam(self):
      return f'Adım {self.ad} {self.soyad} ve yaşım {self.yas} ve bakiyem {self.bakiye}'

# Kullanici nesnesini oluşturma
gokce = Kullanici('Gökçe', 'Tanrıverdi', 'gokce@gmail.com', 37)
# Musteri nesnesini oluşturma
murat = Musteri('Murat', 'Tanrıaldı', 'murat@yahoo.com', 25)

murat.bakiye_ayarla(500)
print(murat.selam())

gokce.dogum_gunu()
print(gokce.selam())

# Kapsülleme -->
gokce.kapsul_degerini_yazdir()
gokce._ozel = 800 # Gökçe için değiştirme
gokce.kapsul_degerini_yazdir()

# Üst sınıftan miras alınan metod
murat.kapsul_degerini_yazdir() # Gökçe'nin değişkenini değiştirmek, Murat'ın değişkenini etkilemez --> Kapsülleme
murat._ozel = 600
murat.kapsul_degerini_yazdir()

# Benzer şekilde, Murat'ın değişkenini değiştirmek Gökçe'nin değişkenini etkilemez.
gokce.kapsul_degerini_yazdir()