import unittest

# get_adjacent_space_keys(area, k):
# get_moveable_space_keys(area, ls_k):
# get_moveable_adjacent_space_keys(area, k):
# get_move_spaces(area, k):

from model import Area, Unit
from combat import CombatRangeUtil

class CombatRangeUtilTest(unittest.TestCase):

	def setUp(self):
		self.area = Area(5, 5)
	
	def test_get_adjacent_space_keys(self):
		self.assertEqual({(0, 1), (1, 0), (1, 2), (2, 1)}, CombatRangeUtil.get_adjacent_space_keys(self.area, (1, 1)))
		self.assertEqual({(0, 1), (1, 0)}, CombatRangeUtil.get_adjacent_space_keys(self.area, (0, 0)))

	def test_get_moveable_space_keys(self):
		self.area.spaces[(0, 1)].accessible = False
		self.assertEqual({(1, 0)}, CombatRangeUtil.get_moveable_space_keys(self.area, {(0, 1), (1, 0)}))

	def test_get_moveable_adjacent_space_keys(self):
		self.area.spaces[(0, 1)].accessible = False
		self.assertEqual({(1, 0)}, CombatRangeUtil.get_moveable_adjacent_space_keys(self.area, (0, 0)))

	def test_get_move_spaces(self):
		self.area.spaces[(2, 2)].unit = Unit('', [], 1, 0)
		expected1 = {(1, 2), (2, 1), (2, 3), (3, 2)}
		self.assertEqual(expected1, CombatRangeUtil.get_move_spaces(self.area, (2, 2)))

		self.area.spaces[(2, 2)].unit = Unit('', [], 2, 1)
		expected2 = {(1, 2), (2, 1), (2, 3), (3, 2)}
		self.assertEqual(expected2, CombatRangeUtil.get_move_spaces(self.area, (2, 2)))

		self.area.spaces[(2, 2)].unit = Unit('', [], 2, 0)
		expected3= {(2, 0), (1, 1), (2, 1), (3, 1), (0, 2), (1, 2), (3, 2), (4, 2), (1, 3), (2, 3), (3, 3), (2, 4)}
		self.assertEqual(expected3, CombatRangeUtil.get_move_spaces(self.area, (2, 2)))

if __name__ == '__main__':
	unittest.main()