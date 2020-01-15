print("Подсчитаем сколько раз выпадает орел и решка в 100 подбрасываниях")
import random
count=1
orel=0
reshka=0
while count <=100:
	num=random.randint(1, 2)
	if num==1:
		orel+=1
	else:
		reshka+=1
	count+=1
print("Orel=",orel,'reshka=',reshka)
