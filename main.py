from model import Action, Area, Unit
from combat_functions import CombatFunctions, CombatRangeUtil
from navigation_util import NavigationUtil


def main():
	move_action = Action('Move', CombatFunctions.move, NavigationUtil.get_move_spaces)
	attack_action = Action('Attack', CombatFunctions.attack, CombatRangeUtil.get_adjacent_space_keys)

	area = Area(3, 3)
	area.spaces[(0, 0)].unit = Unit('Unit-1', [move_action, attack_action], 1, 0)
	area.spaces[(2, 2)].unit = Unit('Unit-2', [move_action, attack_action], 1, 0)

	area = move_action.apply(area, (0, 0), (1, 1))
	# area = attack_action.apply(area, (1, 1), (2, 2))

	print(NavigationUtil.get_move_spaces(area, (1, 1)))


if __name__ == '__main__':
	main()