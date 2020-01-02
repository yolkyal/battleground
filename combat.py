import functools

class CombatFunctions:

	def move(area, k1, k2):
		area.spaces[k2].unit = area.spaces[k1].unit
		area.spaces[k1].unit = None
		area.unit_map[area.spaces[k2].unit] = k2

	def attack(area, k1, k2):
		unit1 = area.spaces[k1].unit
		unit2 = area.spaces[k2].unit
		damage = max(unit1.strength - unit2.armour, 0)
		unit2.strength = max(unit2.strength - damage, 0)

	def armour_attack(area, k1, k2):
		unit1 = area.spaces[k1].unit
		unit2 = area.spaces[k2].unit
		unit2.armour = max(unit2.armour - unit1.strength, 0)


class CombatRangeUtil:
	
	def get_adjacent_space_keys(area, k):
		return {_k for _k in [(k[0], k[1]-1), (k[0], k[1]+1), (k[0]-1, k[1]), (k[0]+1, k[1])] if _k in area.spaces}

	def get_space_spread(area, k, r):
		if r == 1:
			return CombatRangeUtil.get_adjacent_space_keys(area, k)

	def get_moveable_space_keys(area, ls_k):
		return {k for k in ls_k if area.spaces[k].accessible}

	def get_moveable_adjacent_space_keys(area, k):
		return CombatRangeUtil.get_moveable_space_keys(area, CombatRangeUtil.get_adjacent_space_keys(area, k))

	def get_move_spaces(area, k):
		unit = area.spaces[k].unit
		move_range = unit.strength - unit.armour
		ls_k = {k}
		for i in range(move_range):
			ls_k = ls_k.union(functools.reduce(f_union, [CombatRangeUtil.get_moveable_adjacent_space_keys(area, _k) for _k in ls_k]))
		ls_k.remove(k)
		return ls_k


def f_union(s1, s2):
	return s1.union(s2)
