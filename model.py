import copy


class Area:
	def __init__(self, width, height, ls_heights=[], ls_units=[]):
		self.spaces = dict([((x, y), Space()) for x in range(width) for y in range(height)])
		self.unit_map = {}
		for k_height in ls_heights:
			self.spaces[k_height[0]].height = k_height[1]
		for k_unit in ls_units:
			self.spaces[k_unit[0]].unit = k_unit[1]
			self.unit_map[k_unit[1]] = k_unit[0]


class Action:
	def __init__(self, name, func, range_func):
		self.name = name
		self.func = func
		self.range_func = range_func

	def apply(self, area, k1, k2):
		_area = copy.deepcopy(area)
		try:
			self.func(_area, k1, k2)
		except:
			return area
		return _area

	def get_ls_actionable(self, area, k1):
		return self.range_func(area, k1)


class Space:
	def __init__(self, height=0, accessible=True, unit=None):
		self.height = height
		self.accessible = accessible
		self.unit = unit


class Unit:
	def __init__(self, name ,ls_action=[], strength=1, armour=0):
		self.name = name
		self.ls_action = ls_action
		self.strength = strength
		self.armour = armour

	def __hash__(self):
		return hash(self.name)