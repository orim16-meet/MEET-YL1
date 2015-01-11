class Animal:
	
	
	def __init__(self, name, color, age, size, oops):
		self.name=name
		self.color=color
		self.age=age
		self.size=size
		self.oops=oops
	def print_all(self):
		print(self.name)
		print(self.color)
		print(self.age)
		print(self.size)
		print(self.oops)
	def eat(self):
		print(self.name+":Oh it was delicious(I have ate)")	
	def sleep(self):
		print(self.name+":I have slept")

	def Bathroom(self):
		if  (self.oops==False):
			print("Ohhh, Im glad I have went to the bathroom")
		else:
			print("oh, I have pooped, Muma!!!")
			self.oops=True



Snail = Animal(name="Arhimedes Ben-Amram", color="White", age=100, size="Large", oops=False)
Mamuta = Animal(name="Gever Ben-Amram", color="White", age=96, size="Large", oops=True )


Snail.print_all()
Snail.Bathroom()

Snail.Bathroom()
