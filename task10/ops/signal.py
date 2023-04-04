
def check_signal(cycle, x):

    important_cycles = [20, 60, 100, 140, 180, 220]

    if cycle in important_cycles:
        new_strength = cycle * x
        print(new_strength)
    else: 
        new_strength = 0

    return new_strength