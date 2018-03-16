import random 
"""
Gordinho==> haz explotar a tu enemigo dándole comida
"""
print('------Welcome to Gordinho battle-------')

#class pastel
class Pastel:
	def __init__(self, name, dmg):
		self.name = name
		self.dmg = dmg

#all different cakes(bombs)
cake1 = Pastel('chocolat', -10)
cake2 = Pastel('brocoli', 10)
cake3 = Pastel('chile', 15)
cake4 = Pastel('tierra', 20)

def choose_cake(number):
	if number == 1:
		cake = cake1	
	elif number == 2:
		cake = cake2
	elif number == 3:
		cake = cake3
	else:
		cake = cake4
	return cake



#class Gordo (player)
class Gordo:

	def __init__(self, name):

		self.name = name
		self.hp = 100
		
		print('hola gordo {}, tienes 100hp, que la suerte te acompañe'.format(self.name))
	def check_health(self):
		print('Gordo {} Tu vida actual es {}hp'.format(self.name, self.hp))

	def eat_cake(self, cake):
		print('---------------------------------------------')
		self.hp -= cake.dmg
		if(self.hp>=100):
			self.hp=100
		if(self.hp<=0):
			self.hp=0
		if cake.name == 'chocolat':
			print('Gordo {} has comido pastel de {}(+{} hp)'.format(self.name,cake.name, cake.dmg))
		else:	
			print('Gordo {} has comido pastel de {}(-{} hp)'.format(self.name, cake.name, cake.dmg))

	def burla(self, cake):
		print('-----Tragate esto gordito!!!-----')
		print('Gordo {} ha lanzado pastel de {}'.format(self.name, cake.name))

	def muerte_subita(self):
		self.hp += 20

	def restart(self):
		self.hp = 100
		

def play_again():
	print('oooooooooooooooooooooooooooooooooooooooooo')
	play_again = input('Jugar de nuevo? (yes/no)')
	if(play_again=='yes'):
		player1.restart()
		player2.restart()
		play()
	else:
		print('au revoir!!!! ya vete al gym')
	print('oooooooooooooooooooooooooooooooooooooooooo')

def play():
	#rock paper scissors
	while player1.hp>=1 or player2.hp>=1:
		if(player1.hp<=0 or player2.hp<=0):
			break
		#health updates
		
		print('********************************************************')
		player1.check_health()
		player2.check_health()
		#they choose ppt
		print('---------------------------------------------')
		choice_p1 = input('Elige: 1(Piedra), 2(Papel), 3(Tijeras)')
		choice_p2 = random.randint(1,3)

		while not choice_p1 in ('1','2','3'):
			print('Elige Bien cabrón')
			choice_p1 = input('Elige: 1(Piedra), 2(Papel), 3(Tijeras)')
		choice_p1 = int(choice_p1)
		if choice_p1 == 1:
				choice_p1 = 'Piedra'
		elif choice_p1 == 2:
			choice_p1 = 'Papel'
		else:
			choice_p1 = 'Tijeras'

		if choice_p2 == 1:
			choice_p2 = 'Piedra'
		elif choice_p2 == 2:
			choice_p2 = 'Papel'
		else:
			choice_p2 = 'Tijeras'
		print(player1.name+' eligió', choice_p1)
		print(player2.name+' eligió', choice_p2)
		#lets decide who wins
		print('---------------------------------------------')
		#decide the bomb(cake)
		cake = random.randint(1,4)
		cake = choose_cake(cake)
		if choice_p1 == 'Piedra' and choice_p2 == 'Papel':
			player2.burla(cake)
			player1.eat_cake(cake)
		elif choice_p1 == 'Piedra' and choice_p2 == 'Tijeras':
			player1.burla(cake)
			player2.eat_cake(cake)
		elif choice_p1 == 'Papel' and choice_p2 == 'Piedra':
			player1.burla(cake)
			player2.eat_cake(cake)
		elif choice_p1 == 'Papel' and choice_p2 == 'Tijeras':
			player2.burla(cake)
			player1.eat_cake(cake)
		elif choice_p1 == 'Tijeras' and choice_p2 == 'Piedra':
			player2.burla(cake)
			player1.eat_cake(cake)
		elif choice_p1 == 'Tijeras' and choice_p2 == 'Papel':
			player1.burla(cake)
			player2.eat_cake(cake)
		else:
			print('-----Ambos lanzan pastel-----')
			player1.eat_cake(cake)
			player2.eat_cake(cake)
		check_winner()




def check_winner():
	if player1.hp<=0 and player2.hp<=0:
		print('Muerte Súbita...')
		player1.muerte_subita()
		player2.muerte_subita()
		play()
	elif player1.hp<=0:
		print('********************************************************')
		print('*****EL Gordo {} te ha vencido*****'.format(player2.name))
		print('********************************************************')
		play_again()
	elif player2.hp<=0:
		print('********************************************************')
		print('*****Has vencido al Gordo {}, Felicidades!!!*****'.format(player2.name))
		print('********************************************************')
		play_again()
	else:
		pass


#Players
name = input('Cuál es tu nombre? ')

player1 = Gordo(name)
player2 = Gordo('Pepe')

play()
















	








