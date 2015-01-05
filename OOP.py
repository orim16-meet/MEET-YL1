class Animal:
	def __init__(self, name, color, age, size):
		self.name=name
		self.color=color
		self.age=age
		self.size=size
	def print_all(self):
		print(self.name)
		print(self.color)
		print(self.age)
		print(self.size)
Snail = Animal(name="Arhimedes Ben-Amram", color="White", age=100, size="Large")
Roni = Animal(name="Roni Ben-Amram", color="White", age=96, size="Large")


Snail.print_all()
print(BlaBlaBla)
Roni.print_all()

