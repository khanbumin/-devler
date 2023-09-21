import json

# Örnek JSON verisi
kullaniciJSON = '{"ad": "Ahmet", "soyad": "Yılmaz", "yas": 30}'

# JSON verisini sözlüğe çevir
kullanici = json.loads(kullaniciJSON)

# print(kullanici)
# print(kullanici['ad'])

araba = {'marka': 'Ford', 'model': 'Mustang', 'yıl': 1970}

# Araba sözlüğünü JSON formatına dönüştür
arabaJSON = json.dumps(araba, ensure_ascii=False)

print(arabaJSON)
