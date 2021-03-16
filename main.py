#By Pytel 
"""
Trivialni aplikace na prolamovani hesel.

"""
import lib
import time

user = lib.User()
secret = lib.Secret()

user.SetName("Jarda")
user.SetData(["složky", "soubory"])
lenght = 4
kind = 5
heslo = secret.Generate(kind, lenght)
user.SetPassword(heslo, kind)
user.Print()

valid = False
lockpick = lib.PasswdBreaker()
lockpick.SetKind(kind)
lockpick.SetMaxLenght(lenght)
while valid == False:
	paswd = lockpick.GetNext()
	if paswd == None:
		break
	print("Pasword?:", paswd)
	if user.SecurePrint(paswd) == True:
		break
	#time.sleep(1)
	

"""
print( secret.Generate(5, 10) )
END
"""
