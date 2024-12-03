
def parse_input():
    """Parses the input and initializes the maze and tunnels."""
    n, m, k = map(int, input().split())
    board = [list(input()) for _ in range(n)]
    tunnels = dict()
    for _ in range(k):
        i1, j1, i2, j2 = map(int, input().split())
        tunnels[(i1 - 1, j1 - 1)] = (i2 - 1, j2 - 1)
        tunnels[(i2 - 1, j2 - 1)] = (i1 - 1, j1 - 1)
    return n, m, board, tunnels

def initialize_states(n, m, board):
    """Initializes states, transitions, and value arrays."""
    states = [(-1, -1)]  # Death state
    state2idx = dict()
    v = [0.0]  # Probability values
    transitions = [[(0, 1.0)]]  # Self-loop for death state
    s_init = -1

    for i in range(n):
        for j in range(m):
            x = board[i][j]
            if x in ["A", "%", "O"]:
                state2idx[(i, j)] = len(states)
                states.append((i, j))
            elif x in ["#", "*"]:
                state2idx[(i, j)] = 0  # Map obstacles/mines to death state
            if x == "A":
                s_init = state2idx[(i, j)]

    return states, state2idx, transitions, v, s_init

def calculate_transitions(n, m, board, tunnels, states, state2idx, transitions, v):
    """Builds the transitions for each state."""
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for i, j in states[1:]:
        x = board[i][j]
        state_idx = state2idx[(i, j)]
        if x == "%":
            v.append(1.0)
            transitions.append([(state_idx, 1.0)])  # Self-loop for exit
        else:
            v.append(0.0)
            i2, j2 = tunnels.get((i, j), (i, j))
            successors = []
            deaths = 0

            for di, dj in directions:
                ni, nj = i2 + di, j2 + dj
                if 0 <= ni < n and 0 <= nj < m:
                    y = board[ni][nj]
                    if y in ["A", "%", "O"]:
                        successors.append((ni, nj))
                    elif y == "*":
                        deaths += 1

            if not successors:
                transitions.append([(0, 1.0)])  # Stuck: Death state
            else:
                prob = 1 / (len(successors) + deaths)
                t = [(state2idx[s], prob) for s in successors]
                if deaths > 0:
                    t.append((0, deaths * prob))
                transitions.append(t)

def compute_probabilities(states, transitions, v):
    """Iteratively calculates probabilities using the Bellman equation."""
    while True:
        v_old = v.copy()
        for state in range(len(states)):
            v[state] = sum(v[succ] * prob for succ, prob in transitions[state])
        if max(abs(v[state] - v_old[state]) for state in range(len(states))) < 1e-10:
            break

def main():
    """Main function to parse input, initialize states, compute transitions, and calculate probabilities."""
    n, m, board, tunnels = parse_input()
    states, state2idx, transitions, v, s_init = initialize_states(n, m, board)
    calculate_transitions(n, m, board, tunnels, states, state2idx, transitions, v)
    compute_probabilities(states, transitions, v)
    print(f"{v[s_init]:.6f}")

if __name__ == "__main__":
    main()

