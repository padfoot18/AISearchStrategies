"""
Depth First Search algorithm for uninformed search
"""


def dfs(root: 'uninformed_search.Node', goal_state: str, sequence: list):
    sequence.append(root.id)
    if root.city_name != goal_state:
        for child_nodes in root.child:
            if child_nodes.id not in sequence:
                root = child_nodes
                dfs(root, goal_state, sequence)
    else:
        print("Sequence of nodes visited")
        print(", ".join([str(nodes) for nodes in sequence]))
        print("Path to goal state:")
        path = [root.city_name]
        while root.parent:
            root = root.parent
            path.insert(0, root.city_name)
        print(' --> '.join(path))
        exit(0)


def dfs_main(root: 'uninformed_search.Node', goal_state: str):
    """

    :param root: points to the root node of the tree
    :param goal_state: Goal State
    :param sequence: sequence of visited node
    :return: true if goal state is reached
    """
    sequence = list()

    if root not in sequence:
        dfs(root, goal_state, sequence)
