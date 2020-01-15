#Koctu
#Show generation of random num
import random
die1=random.randint(1, 6)
die2=random.randrange(6) + 1
total = die1 + die2
print("При броске выпало", die1, "и", die2, "очков в сумме", total)
input("\n\nНажмите Enter для выхода")
