import numpy as np
from ortools.linear_solver import pywraplp
import time

start = time.time()

def solve_bin_packing(container_size, item_sizes):
    amount_items = len(item_sizes)

    solver = pywraplp.Solver.CreateSolver('SCIP')


    x = {}
    for i in range(amount_items):
        for j in range(amount_items):
            x[(i, j)] = solver.IntVar(0, 1, f'x_{i}_{j}')


    for i in range(amount_items):
        solver.Add(sum(x[i, j] for j in range(amount_items)) == 1)


    for j in range(amount_items):
        solver.Add(sum(x[i, j] * item_sizes[i] for i in range(amount_items)) <= container_size)


    objective = solver.Objective()
    for i in range(amount_items):
        for j in range(amount_items):
            objective.SetCoefficient(x[i, j], i)
    objective.SetMinimization()


    status = solver.Solve()


    if status == pywraplp.Solver.OPTIMAL:
        containers = [[] for _ in range(amount_items)]
        for j in range(amount_items):
            for i in range(amount_items):
                if x[(i, j)].solution_value() > 0:
                    containers[j].append(i)
        return [container for container in containers if container]
    else:
        return None

file = open('itemset_size.txt')
amount_items = int(file.readline())
container_size = int(file.readline())
items = np.loadtxt('itemset.txt')
file.close()


containers = solve_bin_packing(container_size, items)

if containers is not None:
    for i, container_items in enumerate(containers):
        print(f'Container {i}: {container_items}')
else:
    print('Could not find a solution')

end = time.time() - start

print("Total time: ", end)
