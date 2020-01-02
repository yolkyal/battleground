import unittest

# move(area, k1, k2)
# attack(area, k1, k2)
# armour_attack(area, k1, k2)

from model import Action, Area, Unit
from combat import CombatFunctions, CombatRangeUtil

class CombatFunctionsTest(unittest.TestCase):

	def setUp(self):
		self.area = Area(3, 3)
		self.area.spaces[(0, 0)].unit = Unit('Unit-1', [], 2, 1)
		self.area.spaces[(2, 2)].unit = Unit('Unit-2', [], 2, 1)

	def test_move(self):
		move_action = Action('Move', CombatFunctions.move, None)
		_area = move_action.apply(self.area, (0, 0), (1, 1))
		self.assertIsNotNone(_area.spaces[(1, 1)].unit)
		self.assertIsNone(self.area.spaces[(1, 1)].unit)

	def test_attack(self):
		attack_action = Action('Attack', CombatFunctions.attack, None)
		_area = attack_action.apply(self.area, (0, 0), (2, 2))
		self.assertEqual(1, _area.spaces[(2, 2)].unit.strength)
		self.assertEqual(2, self.area.spaces[(2, 2)].unit.strength)

	def test_armour_attack(self):
		armour_attack_action = Action('Armour Attack', CombatFunctions.armour_attack, None)
		_area = armour_attack_action.apply(self.area, (0, 0), (2, 2))
		self.assertEqual(0, _area.spaces[(2, 2)].unit.armour)
		self.assertEqual(1, self.area.spaces[(2, 2)].unit.armour)

if __name__ == '__main__':
	unittest.main()