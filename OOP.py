
class Animal(object):
	def __init__(self,sound,name,age,favorite_color,food):
		self.sound = sound
		self.name = name
		self.age = age 
		self.favorite_color = favorite_color
		self.sound = sound
		self.food = food
	def eat(self,food):
		print("Yummy!!" + self.name + " is eating " + self.food)
	def description(self):
		print(self.name + " is " + self.age +" years old and loves the color " + self.favorite_color)
	def animal_sound(self):
		print("I am " + self.name + self.sound + self.sound + self.sound)


sara = Animal("moo ", "Sara ", "18", "brown", "milk")


sara.description()
sara.eat('milk')
sara.animal_sound()


class Song(object)

