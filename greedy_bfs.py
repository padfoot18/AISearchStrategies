"""
Greedy best first Search Algorithm
"""
import pprint
from heapq import heappop, heappush


def greedy_bfs(root, goal_state, map, heurestic, heap=None, sequence=None, path=None, graph=None):
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
        return

    children = dict(map.loc[root, :])
    for child, dist in children.items():
        if dist != 0:
            sequence.append([child, heurestic[child]])
            h = heurestic[child]
            heappush(heap, [h, child])

    min_child = heappop(heap)[-1]

    greedy_bfs(min_child, goal_state, map, heurestic, heap, sequence, path)
