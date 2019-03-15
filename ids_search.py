"""
Iterative Deepening search algorithm for uninformed search
"""
# import uninformed_search


def ids(root, goal_state, max_depth):
    """
    Iterative Deepening Depth First Search
    :param root: points to the root node of the state space tree
    :param goal_state: Goal state
    :param max_depth: Maximum depth
    :return:
    """
    sequence = list()
    for depth_limit in range(max_depth):
        if dls(root, goal_state, depth_limit, sequence):
            sequence = [str(x) for x in sequence]
            print('Sequence of nodes visited: ', ', '.join(sequence), sep='\n')
            return True
    return False


def dls(root: 'uninformed_search.Node', goal_state: str, depth_limit: int, sequence):
    """
    Depth Limited Search
    :param root: points to the root node of the state space tree
    :param goal_state: Goal state
    :param depth_limit:
    :return:
    """
    sequence.append(root.id)

    if root.city_name == goal_state:
        depth = root.level
        print('Solution found at depth =', depth)
        print('Path to goal state:')
        path = [root.city_name]
        while root.parent:
            root = root.parent
            path.insert(0, root.city_name)
        print(' --> '.join(path))

        return True
    depth_limit -= 1
    if depth_limit >= 0:
        for node in root.child:
            if dls(node, goal_state, depth_limit, sequence):
                return True
    return False
