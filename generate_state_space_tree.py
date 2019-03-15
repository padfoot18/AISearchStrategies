import pydot
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


def generate_tree(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12):
    graph = pydot.Dot(graph_type='digraph')
    node1 = pydot.Node(str(n1), style="filled", fillcolor="red")
    node2 = pydot.Node(str(n2), style="filled", fillcolor="red")
    node3 = pydot.Node(str(n3), style="filled", fillcolor="red")
    node4 = pydot.Node(str(n4), style="filled", fillcolor="red")
    node5 = pydot.Node(str(n5), style="filled", fillcolor="red")
    node6 = pydot.Node(str(n6), style="filled", fillcolor="red")
    node7 = pydot.Node(str(n7), style="filled", fillcolor="red")
    node8 = pydot.Node(str(n8), style="filled", fillcolor="red")
    node9 = pydot.Node(str(n9), style="filled", fillcolor="red")
    node10 = pydot.Node(str(n10), style="filled", fillcolor="red")
    node11 = pydot.Node(str(n11), style="filled", fillcolor="red")
    node12 = pydot.Node(str(n12), style="filled", fillcolor="red")

    graph.add_node(node1)
    graph.add_node(node2)
    graph.add_node(node3)
    graph.add_node(node4)
    graph.add_node(node5)
    graph.add_node(node6)
    graph.add_node(node7)
    graph.add_node(node8)
    graph.add_node(node9)
    graph.add_node(node10)
    graph.add_node(node11)
    graph.add_node(node12)

    graph.add_edge(pydot.Edge(node1, node2))
    graph.add_edge(pydot.Edge(node1, node3))
    graph.add_edge(pydot.Edge(node1, node4))
    graph.add_edge(pydot.Edge(node2, node5))
    graph.add_edge(pydot.Edge(node2, node6))
    graph.add_edge(pydot.Edge(node2, node7))
    graph.add_edge(pydot.Edge(node3, node8))
    graph.add_edge(pydot.Edge(node6, node9))
    graph.add_edge(pydot.Edge(node6, node10))
    graph.add_edge(pydot.Edge(node7, node11))
    graph.add_edge(pydot.Edge(node8, node12))

    graph.write_png('state_space_tree.png')

    img = mpimg.imread('state_space_tree.png')
    plt.imshow(img)
