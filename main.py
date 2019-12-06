from model import Action, Area, Unit
from combat_functions import move, attack


def main():
	move_action = Action('Move', move)
	attack_action = Action('Attack', attack)

	area = Area(3, 3)
	area.spaces[(0, 0)].unit = Unit('Unit-1', [move_action, attack_action])
	area.spaces[(2, 2)].unit = Unit('Unit-2', [move_action, attack_action])

	area = move_action.apply(area, (0, 0), (1, 1))
	area = attack_action.apply(area, (1, 1), (2, 2))

	print(area)


if __name__ == '__main__':
	main()