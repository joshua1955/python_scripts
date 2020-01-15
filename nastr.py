import random
print("Your mood today is:\n")
mood=random.randint(1,3)
if mood ==1:
	print("радостное")
elif mood == 2:
	print('злое')
elif mood == 3:
	print('грустное')
else:
	print('а черт его знает')
