import minimax_game

class BattleAction:
	def __init__(self, action, k1, k2=None):
		self.action = action
		self.k1 = k1
		self.k2 = k2


class Battle(minimax_game.MinimaxGame):
	def get_actions(state, turn_unit_k):
		turn_unit = state.unit_map[turn_unit_k]
		return [BattleAction(action, turn_unit_k, k) for action in turn_unit.ls_action for k in action.get_ls_actionable(state, turn_unit_k)]

	def get_state_after_action(state, battle_action):
		return battle_action.apply(state)

	def eval_state(state):
		return BattleStateEvaluator.evaluate(state)


class BattleStateEvaluator:
	def evaluate(state):
		return 0