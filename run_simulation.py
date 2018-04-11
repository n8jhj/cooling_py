def run_simulation(plant):
    '''Runs the cooling system simulation.'''
    # get feasible combinations
    feasible = get_feasible_combinations(plant)
    # choose best feasible combinations
    # run chosen combination
    # keep track of results
    results = 1
    return results

def get_feasible_combinations(plant):
    # make list of all possible combinations (matrix form)
    n_gen = len(plant.generator)
    n_combinations = (1, 3, 7, 15, 28)
    n_possible = n_combinations[n_gen]
    mat_combos = [[0] * n_gen] * n_possible
    for i in range(n_possible):
        feasible = False
        if sum([gen.capacity for gen in plant.generator]) < demand:
            # sum of setpoints could never be enough
            feasible = False
        else:
            curr_availability = sum([gen.setpoint for gen in plant.generator])
            if curr_availability >= demand:
                # sum of current setpoints is enough
                feasible = True
            else:
                # see if generator set could ramp to desired setpoint
                extra_availability = sum([gen.ramp for gen in plant.generator])
                if curr_availability + extra_availability >= demand:
                    feasible = True
                else:
                    feasible = False
    # test each one to see if it's feasible
    # sum of available generation must be at least as much as demand
    feasible_combinations = 1
    return feasible_combinations
