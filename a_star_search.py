"""
A* search algorithm
"""
import pprint

def a_star_search(root, goal_state, map, heurestic, g=0, sequence=None, path=None):
    print(root)
    if path is None:
        path = []
    if sequence is None:
        sequence = []
    path.append(root)

    if root == goal_state:
        print('Sequence of nodes visited:')
        pprint.pprint(sequence)
        print('Path to goal state:')
        print(' --> '.join(path))
        print()
        return
    children = dict(map.loc[root, :])
    min_cost = 999999

    for child, dist in children.items():
        sequence.append([child, heurestic[child]])
        if dist != 0:
            h = heurestic[child]
            if (g+h) < min_cost:
                min_cost = g+h
                min_child = child

    g += children[min_child]
    a_star_search(min_child, goal_state,map, heurestic, g, sequence, path)
