from pandas.io.formats.format import return_docstring

ROWS = 6
COLS = 7


def print_state(state):
  print(' '.join(map(str, range(0, COLS))))
  for i in range(ROWS):
    for j in range(COLS):
      s = []
      if state[i][j] == 'X':
        print('\033[91m', end='') # RED COMMAND
      elif state[i][j] == 'O':
        print('\033[93m', end='') # YELLOW COMMAND
      print(state[i][j], end='')
      print('\033[0m', end=' ') # END COMMAND
    print()
  print()

state = [
    ['·', '·', '·', '·', '·', '·', '·'],
    ['·', '·', '·', '·', '·', '·', '·'],
    ['·', '·', '·', '·', '·', '·', '·'],
    ['·', 'X', '·', '·', '·', '·', '·'],
    ['·', 'X', '·', '·', '·', '·', '·'],
    ['·', 'X', 'O', 'O', 'O', '·', '·']
]
print_state(state)


def evaluate(state):
    #horizontal
    for r in range(ROWS):
        for c in range(COLS-3):
            if state[r][c]==state[r][c+1]==state[r][c+2]==state[r][c+3]:
                if state[r][c]=='X':
                    return 1
                if state[r][c]=='O':
                    return -1
    #vertical
    for c in range(COLS):
        for r in range(ROWS-3):
            if state[r][c]==state[r+1][c]==state[r+2][c]==state[r+3][c]:
                if state[r][c]=='X':
                    return 1
                if state[r][c]=='O':
                    return -1
    #diagonal1
    for r in range(ROWS-3):
        for c in range(COLS-3):
            if (state[r  ][c  ] == state[r+1][c+1] ==
                state[r+2][c+2] == state[r+3][c+3]):
                if state[r][c] == 'X':
                    return 1
                if state[r][c] == 'O':
                    return -1
    for r in range(ROWS-3):
        for c in range(3, COLS):
            if (state[r  ][c  ] == state[r+1][c-1] ==
                state[r+2][c-2] == state[r+3][c-3]):
                if state[r][c] == 'X':
                    return 1
                if state[r][c] == 'O':
                    return -1
    for r in range(ROWS):
        for c in range(COLS):
            if state[r][c]=='·':
                return None
    return 0



  #""" Evaluates the utility value for a given state """
  # TASK 1: Implement this function


def is_terminal(state):
    # """ Checks if the state is a terminal state """
    return evaluate(state) in [0, 1, -1]
# TASK 2: Implement this function


def get_successors(cur_state):
    successors = []
    for col in range(COLS):
        next_board = apply_action(cur_state, col)
        if next_board is not None:
            successors.append(next_board)
    return successors

  #""" Returns a list of successor states """

  # TASK 3: Implement this function


def apply_action(state,action):
    if not(0<=action<=COLS):
        return None
    if state[0][action]!='·':
        return None
    for row in range(ROWS-1, -1, -1):
        if state[row][action]=='·':
            new_state = [r[:] for r in state]
            num_x = sum(row.count('X') for row in state)
            num_o = sum(row.count('O') for row in state)
            next_placement = 'O' if num_x==num_o else 'X'
            new_state[row][action] = next_placement
            return new_state
    return None


def alphabeta_decision(state, depth_limit = 4):
  #"""
  #Returns the best move (or best next state) for the AI agent.
  #Use the alpha-beta pruning with depth limit to find the best move.
  #"""
    if is_terminal(state):
        return state
    best_value = float('inf')
    best_next_state = None

    for next_state in get_successors(state):
        value = min_ab_value(next_state, -float('inf'), float('inf'), depth_limit-1)
        if value < best_value:
            best_value = value
            best_next_state = next_state

    return best_next_state if best_next_state is not None else state
  # TASK 4: Implement this function

def max_ab_value(state, alpha, beta, depth):
    if is_terminal(state):
        return evaluate(state)
    if depth <= 0:
        return 0

    value = -float('inf')

    for next_state in get_successors(state):
        child_value = min_ab_value(next_state, alpha, beta, depth - 1)
        value = max(value, child_value)
        alpha = max(alpha, value)
        if beta <= alpha:
            break
    return value


#"""
  #Returns the best value for the AI agent (maximizer).
  #Use the alpha-beta pruning with depth limit to find the best value.
  #"""

  # TASK 5: Implement this function


def min_ab_value(state, alpha, beta, depth):
    if is_terminal(state):
        return evaluate(state)
    if depth <= 0:
        return 0

    value = float('inf')

    for next_state in get_successors(state):
        child_value = max_ab_value(next_state, alpha, beta, depth-1)
        value = min(value, child_value)
        beta = min(beta, value)
        if value <= alpha:
            break

    return value

  #"""
  #Returns the best value for the opponent agent (minimizer).
  #Use the alpha-beta pruning with depth limit to find the best value.
  #"""

  # TASK 6: Implement this function

# Feel free to customize the function below if necessary

def play_vs_ai(initial_state = None, depth_limit = 4):
  """
  Starts a match: AI agent vs. user.
  Feel free to customize this function, or ignore it whatsoever.
  But you should be able to demonstrate a few matches in this notebook.
  """

  if initial_state:
    state = initial_state
  else:
    state = [['·'] * COLS for _ in range(ROWS)]
  print_state(state)
  ai_agent_turn = True

  while True:
    if ai_agent_turn:
      state = alphabeta_decision(state, depth_limit=depth_limit)
    else:
      i = int(input('Pick a column [0-6]:'))
      if i < 0 or i >= COLS:
        print('Invalid column, try again!')
      elif state[0][i] != '·':
        print('That column is full, try another one!')
        ai_agent_turn = not ai_agent_turn
      else:
        for j in range(ROWS - 1, -1, -1):
          if state[j][i] == '·':
            state[j][i] = 'X'
            break

    print_state(state)

    ai_agent_turn = not ai_agent_turn
    if is_terminal(state):
      break

  v = evaluate(state)
  # if v == -float('inf'):
  #  print('You won!')
  # elif v == float('inf'):
  #  print('You lost!')
  # else:
  #  print('Draw!')
  if v==1:
      print("You won!")
  elif v==-1:
      print("YOu lost")
  else:
      print("Draw")

play_vs_ai(depth_limit=4)