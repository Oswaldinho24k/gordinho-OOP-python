from bots import Robot
class Person:
	poblacion = 0

	def __init__(self, name, age, hobby, sex):

		self.name = name
		self.age = age
		self.hobby = hobby
		self.sex = sex

	def saludar(self):
		print('Hi my name is ', self.name)
		print('tengo ' ,self.age )
		print('me gusta ', self.hobby)
		print('frecuencia de sexo: ', self.sex)

	@classmethod
	def cuenta(cls):
		print('numero de personas ahora:',cls.poblacion)

# Robot.cuantos()
# nombre = input('Cómo te llamas')

# p = Person(nombre, 21, 'go to the gym', 'nunca, im virgin')
# p.saludar()
# Person.cuenta()
# a = input('elige tu personaje')
# a = int(a)
# c= a+5

# Robot.cuantos()

player = input('elige a tu jugador')

if player == '1':
	player1 = Gladiador()
if player == '2':
	player1 = Guerrero