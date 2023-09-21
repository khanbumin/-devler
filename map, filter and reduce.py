from functools import reduce  # reduce işlevini kullanmak için functools modülünü içe aktarıyoruz

l1 = [2, 3, 4, 5, 6]

# l1 listesine verilen komutu uygulayan map işlevini kullanıyoruz
mapping_the_l1 = list(map(lambda x: x * 2, l1))  
# Bu durumda l1 listesinin her bir öğesini 2 ile çarpıyoruz, lambda işlevi kullanıyoruz

print(mapping_the_l1)

# filter işlevini kullanarak l1 listesini isteğimize göre filtreliyoruz
filtering_the_l1 = list(filter(lambda x: x % 2 == 0, l1))  
# Bu durumda l1 listesinde 2'ye bölünebilen sayıları filtreliyoruz.

print(filtering_the_l1)

def toplama(x, y):
   return x + y

# reduce işlevini kullanarak l1 listesinde matematiksel işlemler yapıyoruz
reducing_the_l1 = reduce(toplama, l1)  
# Bu durumda l1 listesindeki tüm öğeleri topluyoruz.

print(reducing_the_l1)
