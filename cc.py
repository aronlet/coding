from 123 import x

print(x)

class Player:
	def __init__(self, ap,name):
	    print('你是在靠杯窩')
	    self.name = name
	    self.hp = 100
	    self.ap = ap

	def attack(self,target):
		print(self.name,"attacking",target.name)
		target.hp = target.hp - self.ap

p1 = Player('Player1', 5)
p2 = Player('Player2', 10)
p1.attack(5)
print(p2.ap)