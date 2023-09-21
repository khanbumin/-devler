# Bir modül temel olarak uygulamanıza dahil etmek için kullanabileceğiniz bir dizi işlev içeren bir dosyadır. Çekirdek Python modülleri, pip paket yöneticisi kullanarak kurabileceğiniz modüller (Django dahil) ve özel modüller bulunur.

# Çekirdek modüller
import datetime
from datetime import date
import time
from time import time

# Pip modülü
from camelcase import CamelCase

# Özel modülü içe aktarma
import dogrulayici
from dogrulayici import emaili_dogrula

# today = datetime.date.today()
bugun = date.today()
zamanDamgasi = time()

c = CamelCase()
# print(c.hump('hello there world'))

email = 'test#test.com'
if emaili_dogrula(email):
  print('E-posta geçerli')
else:
  print('E-posta geçerli değil')
