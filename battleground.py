import copy
from functools import reduce

class Area:
	def __init__(self, width, height):
		self.spaces = dict([((x, y), Space()) for x in range(width) for y in range(height)])

	def __repr__(self):
		return str(self.spaces)


class Action:
	def __init__(self, name, func):
		self.name = name
		self.func = func

	def apply(self, area, k1):
		_area = copy.deepcopy(area)
		try:
			self.func(_area, k1)
		except:
			return area
		return _area

	def apply(self, area, k1, k2):
		_area = copy.deepcopy(area)
		try:
			self.func(_area, k1, k2)
		except:
			return area
		return _area

	def __repr__(self):
		return name


class Space:
	def __init__(self, accessible=True, unit=None):
		self.accessible = accessible
		self.unit = unit

	def __repr__(self):
		return str(self.unit)


class Unit:
	def __init__(self, name ,ls_action, strength=1, armour=0):
		self.name = name
		self.ls_action = ls_action
		self.strength = strength
		self.armour = armour

	def __repr__(self):
		return str((self.name, self.strength, self.armour))

def main():
	attack_action = Action('Attack', attack)
	move_action = Action('Move', move)

	area = Area(3, 3)
	area.spaces[(0, 0)].unit = Unit('Unit-1', [move_action, attack_action])
	area.spaces[(2, 2)].unit = Unit('Unit-2', [move_action, attack_action])

	area = move_action.apply(area, (0, 0), (1, 1))
	area = attack_action.apply(area, (1, 1), (2, 2))

	print(area)


if __name__ == '__main__':
	main()