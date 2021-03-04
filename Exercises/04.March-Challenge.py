# Not: python ile n sayıda list_item'ı m sayıda gruba (n > 2m) random atacak bir code yazmak isteyen var mı? bu bir challenge'dır. 
import numpy as np

item_count = int(input("Kaç eleman oluşturulsun ? : "))
group_count = int(input("Kaç gruba ayrılsın istersiniz ? : "))

while 1:
    if item_count > 2 * group_count:
        break
        
    else:
        print("Daha büyük bir list_item oluşturun")
        item_count = int(input("Kaç eleman oluşturulsun ? : "))
        group_count = int(input("Kaç gruba ayrılsın istersiniz ? : "))

arr = [*range(item_count)]

listsofarrays = []

for i in range(group_count):
    listsofarrays.append([])

result = np.random.randint(0,group_count,item_count)

for j in range(item_count):
    listsofarrays[result[j]].append(arr[j])

print("Ve büyük çekiliş sonucumuz : ", result)

for k in range(group_count):
    print(k+1,". grup elemanlarımız ----> ", listsofarrays[k])