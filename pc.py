  GNU nano 2.9.3                                          pc.py                                                     

import random
chel=0
min=1
max=1000
pc=random.randint(min,max)
print("""Инструкция
1 - меньше
2 - больше
3 - угадал""")
while pc!=chel:
        print("Ваше число больше или меньше, чем", pc)
        choose=int(input(''))
        if choose==1:
                max=pc
                pc=random.randint(min,pc)
                while pc==max:
                         pc=random.randint(min,pc)
        elif choose==2:
                min=pc
                pc=random.randint(pc,max)
                while pc==min:
                        pc=random.randint(pc,max)
        else:
                chel=pc
                print("Ваше число", chel)

