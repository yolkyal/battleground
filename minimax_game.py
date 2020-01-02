class MinimaxGame:

	def create_base_state():
		raise NotImplementedError('Missing method implementation: "create_base_state()"')

	def get_actions(state, player):
		raise NotImplementedError('Missing method implementation: "get_actions(state)"')

	def get_state_after_action(state, action):
		raise NotImplementedError('Missing method implementation: "get_state_after_action(state, action)"')

	def eval_state(state):
		raise NotImplementedError('Missing method implementation: "eval_state(state)"')

	def print_state(state):
		pass