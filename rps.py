import random

def player(prev_play, opponent_history = []):
    # Define the strategies for each opponent
    strategies = {
        'random': lambda: random.choice(['R', 'P', 'S']),
        'copycat': lambda: opponent_history[-1],
        'cycle': lambda: ['R', 'P', 'S'][opponent_history.count('R') % 3],
        'alternate': lambda: ['R', 'P', 'S'][(opponent_history.count('R') + opponent_history.count('P')) % 3],
        'predict': lambda: ['R', 'P', 'S'][(opponent_history.count('R') - opponent_history.count('S')) % 3],
    }
    
    # Choose the strategy based on the opponent
    if prev_play == '':
        strategy = random.choice(list(strategies.values()))
    elif opponent_history[-1] == 'R':
        strategy = strategies['copycat']
    elif opponent_history[-1] == 'P':
        strategy = strategies['cycle']
    elif opponent_history[-1] == 'S':
        strategy = strategies['alternate']
    
    # Play the next move
    next_move = strategy()
    
    return next_move