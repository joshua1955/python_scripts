#Pass
#show construction of IF
print("Hello!\n")
password=''
username=''
while not username:
	username=input("Username:")
while not password:
	password=input("Password:")
if password == "secret":
	print("Успех")
else:
	print("Доступ закрыт!")
