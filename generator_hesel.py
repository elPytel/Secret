#By Pytel

import string 
import random

DEBUG = False

"""
kind:
1) cisla
2) mala
3) velka
4) mala velka
5) mala velka cisla
6) vsechno
"""
class Secret:
	def __init__ (self):
		self.password = ""
		self.numbers = list(string.digits)
		self.US_lower = list(string.ascii_lowercase)
		self.US_upper = list(string.ascii_uppercase)
		self.US_letters = list(string.ascii_letters)
		self.printable = list(string.digits) + list(string.ascii_letters) + list(string.punctuation)
		
		self.punctuation = list(string.punctuation)
	
	def KindToString (self, kind):
		string = []
		if (kind == 1):
			string = self.numbers
		elif (kind == 2):
			string = self.US_lower
		elif (kind == 3):
			string = self.US_upper
		elif (kind == 4):
			string = self.US_letters
		elif (kind == 5):
			string = self.numbers + self.US_letters
		elif (kind == 6):
			string = self.printable
		else:
			if DEBUG:
				print(kind)
				print("Ups, something Faiglet!")
			string.append(-1)
		return string
	
	def Generate (self, kind, lenght):
		if DEBUG:
			print("kind:", kind)
			print("lenght:", lenght)
		password = ""
		string = self.KindToString(kind)
		if (len(string) == 1 and string[0] == -1):
			print("ERROR: wrong kind!")
		else:
			for i in range(lenght):
				index = random.randint(0, len(string)-1)
				password = password + string[index]
		
		return password
	

		
print(" ---Tato aplikačka generuje hesla---")
lenght = int(input("  Zadjete delku hesla: "))
kind = int(input("  Zadejte složitost hesla (1-6) : "))
secret = Secret()
print(" Vaše heslo:", secret.Generate(kind, lenght) )

