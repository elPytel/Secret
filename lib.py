#By Pytel

import string 
import random

DEBUG = True

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
			string.append(-1)
		return string
	
	def IsValid (self, kind):
		#TODO
		return True
	
	def Generate (self, kind, lenght):
		password = ""
		string = self.KindToString(kind)
		if (len(string) == 1 and string[0]== -1):
			print("ERROR: wrong kind!")
		else:
			for i in range(lenght):
				index = random.randint(0, len(string)-1)
				password = password + string[index]
		
		return password
	
	def SetPassword (self, password):
		self.password = password
	
	def GetPassword (self):
		return self.password
		
#podle indexu prochazi kombinace
class PasswdBreaker:
	def __init__ (self):
		self.position = [-1]		# LSB on left
		self.secret = Secret()
		self.kind = 6
		self.max_lenght = 0
		self.string = self.secret.KindToString(self.kind)
	
	def Next (self):
		ret = True
		carry = 1;
		index = -1;
		while carry == 1:
			index = index +1
			if 0 and DEBUG:
				print("Index:", index)
				print("len  :", len(self.position))
			if index >= self.max_lenght:
				ret = False
				break
			if len(self.position) <= index:
				self.position.append(0)
				break						# pridava radky zacinajici 0
			if self.position[index] < len(self.string)-1:
				self.position[index] = self.position[index] + carry
				carry = 0
			else:
				self.position[index] = 0
				carry = 1
		return ret
	
	def MakePassword (self):
		password = ""
		for i in range(len(self.position)-1,-1,-1):
			if 0 and DEBUG:
				print("index:", i)
				print("size :", self.position[i])
				print("char :", self.string[self.position[i]] )
			password = password + self.string[self.position[i]]
		return password
	
	def GetNext (self):
		if (self.Next() == False):
			return None
		password = self.MakePassword()
		if 0 and DEBUG:
			print("Position:", self.position)
			print("Paswd:   ", password)
		return password
	
	def SetKind (self, kind):
		if kind < 7:
			self.kind = kind
			self.GenerateString()
		else:
			print("Ups, something Faiglet!")
			
	def SetMaxLenght (self, lenght):
		self.max_lenght = lenght
			
	def GenerateString (self):
		self.string = self.secret.KindToString(self.kind)
		if DEBUG:
			print(self.string)

class User:
	def __init__ (self):
		self.name = ""
		self.password = ""
		self.data = []
		
		self.secret = Secret()
		
	def IsValidPassword (self, password, kind):
		secret = self.secret
		secret.SetPassword(password)
		return secret.IsValid(kind)
	
	def SetPassword (self, password, kind):
		if ( self.IsValidPassword(password, kind) ):
			self.password = password
			return True
		else: 
			return False
		
	def SetName (self, name):
		self.name = name
		
	def SetData (self, data):
		self.data = data
		
	def SecurePrint (self, password):
		if 0 and DEBUG:
			print(self.password)
			print(password)
		if (self.password == password):
			self.Print()
			return True
		else:
			print("Invalid password")
			return False
		
	def Print (self):
		print("Name:", self.name)
		print("Pswd:", self.password)
		print("Data:", self.data)
	
"""
secret = Secret()
print(secret.US_letters + secret.numbers)
END
"""