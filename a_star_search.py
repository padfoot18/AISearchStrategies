"""
A* search algorithm
"""
import pprint
from heapq import heappop, heappush


def a_star_search(root, goal_state, map, heurestic, g_global=0, heap=None, sequence=None, path=None):
    if path is None:
        path = []
    if sequence is None:
        sequence = []
    if heap is None:
        heap = []
    path.append(root)

    if root == goal_state:
        print('Sequence of nodes visited:')
        pprint.pprint(sequence)
        print('Path to goal state:')
        print(' --> '.join(path))
        print()

        i = len(path) - 2
        child = path[-1]
        actual_path = [child]

        while i >= 0:
            node = path[i]
            if map.loc[node, child]:
                actual_path.insert(0, node)
                child = node
            i -= 1

        print('Actual path traversed: ')
        print(' --> '.join(actual_path))
        return
    children = dict(map.loc[root, :])

    for child, dist in children.items():
        if dist != 0:
            g = g_global + children[child]
            h = heurestic[child]
            sequence.append([child, g+h])
            heappush(heap, [g+h, child])

    min_child = heappop(heap)[-1]
    g_global += children[min_child]
    a_star_search(min_child, goal_state, map, heurestic, g_global, heap, sequence, path)
