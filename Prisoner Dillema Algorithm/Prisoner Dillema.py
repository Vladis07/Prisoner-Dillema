seed = 123456789

def simple_rand():
    global seed
    seed = (1103515245 * seed + 12345) % (2**31)
    return seed

def random_choice(options):
    index = simple_rand() % len(options)
    return options[index]

def selfish(my_history, opponent_history, rounds=None):
    turn = len(my_history)
    if turn == 0:
        return 0
    if opponent_history[-1] == 0:
        return 0
    def detect_pattern(history, min_len=2, max_len=5):
        for pattern_len in range(min_len, min(max_len, len(history) // 2) + 1):
            pattern = history[-pattern_len:]
            if history[-2 * pattern_len:-pattern_len] == pattern:
                return pattern
        return None
    pattern = detect_pattern(opponent_history)
    if pattern:
        predicted_move = pattern[turn % len(pattern)]
        if predicted_move == 1:
            return 0
        else:
            return 1 if turn % 6 == 0 else 0
    return 1 if turn % 7 == 0 else 0

def simulate_selfish(total_rounds=60):
    my_history = []
    opponent_history = []
    for _ in range(total_rounds):
        my_move = selfish(my_history, opponent_history)
        opp_move = random_choice([0, 1])
        my_history.append(my_move)
        opponent_history.append(opp_move)
    return my_history, opponent_history

def print_game_simulation(my_history, opponent_history):
    print(f"{'Round':>5} | {'Selfish':>7} | {'Random Opponent':>16}")
    print("-" * 40)
    for i, (me, opp) in enumerate(zip(my_history, opponent_history), 1):
        print(f"{i:>5} | {me:>7} | {opp:>16}")
    print("-" * 40)

my_hist, opp_hist = simulate_selfish(60)
print_game_simulation(my_hist, opp_hist)
