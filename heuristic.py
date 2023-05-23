import numpy as np
import time

start = time.time()
def find_max(containers, item_to_add_size, container_size):
    remaining_place_pred = np.infty
    index = -1
    for i in range(len(containers)):
        if (container_size - sum(containers[i]) < remaining_place_pred) and (container_size - sum(containers[i]) > item_to_add_size):
            remaining_place_pred = container_size - sum(containers[i])
            index = i
    return index


def best_fit_algorithm(items, container_size):
    sorted_items = sorted(items, reverse=True)
    containers = []

    for item_to_add in sorted_items:
        index = find_max(containers, item_to_add, container_size)
        if index != -1:
            containers[index].append(item_to_add)
        else:
            containers.append([item_to_add])
    return containers

file = open('itemset_size.txt')
amount_items = int(file.readline())
container_size = int(file.readline())
file.close()

items_sizes = np.loadtxt('itemset.txt')

containers = best_fit_algorithm(items_sizes, container_size)

for i, container in enumerate(containers):
    print(f"Контейнер {i}: {container}")

end = time.time() - start

print(end)
