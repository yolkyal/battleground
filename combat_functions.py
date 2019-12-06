def move(area, k1, k2):
	area.spaces[k2].unit = area.spaces[k1].unit
	area.spaces[k1].unit = None

def attack(area, k1, k2):
	unit1 = area.spaces[k1].unit
	unit2 = area.spaces[k2].unit
	damage = max(unit1.strength - unit2.armour, 0)
	unit2.strength = max(unit2.strength - damage, 0)