from functools import reduce


class NavigationUtil:
	def get_adjacent_space_keys(area, k):
		return {_k for _k in [(k[0], k[1]-1), (k[0], k[1]+1), (k[0]-1, k[1]), (k[0]+1, k[1])] if _k in area.spaces}

	def get_moveable_space_keys(area, ls_k):
		return {k for k in ls_k if area.spaces[k].accessible}

	def get_moveable_adjacent_space_keys(area, k):
		return NavigationUtil.get_moveable_space_keys(area, NavigationUtil.get_adjacent_space_keys(area, k))

	def get_move_spaces(area, k):
		move_range = area.spaces[k].unit.strength
		ls_k = {k}
		for i in range(move_range):
			ls_k = ls_k.union(reduce(f_union, [NavigationUtil.get_moveable_adjacent_space_keys(area, _k) for _k in ls_k]))
		ls_k.remove(k)
		return ls_k


def f_union(s1, s2):
	return s1.union(s2)