"""
Iterative Deepening search algorithm for uninformed search
"""
import uninformed_search


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
    for node in root.child:
        sequence.append()


