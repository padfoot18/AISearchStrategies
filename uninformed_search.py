"""
bfs ids for map exploration
"""
import pandas as pd

df = pd.read_csv('input.csv')
city_names = df.columns
print(city_names)

city_distance = df.iloc[1:, 1:]
print(city_distance)


class Node:
    def __init__(self, city_name, parent):
        self.city_name = city_name
        self.parent = parent
        self.child = []

    def __repr__(self):
        child_names = [x.city_name for x in self.child]
        return "City Name: {}, Parent: {}, Child: {}".format(self.city_name, self.parent, child_names)

    def append_child(self, children):
        for child in children:
            self.child.append(child)


n1 = Node('Arad', parent=None)
n2 = Node('Sibiu', parent=n1)
n3 = Node('Timisoara', parent=n1)
n4 = Node('Zerind', parent=n1)
n5 = Node('Oradia', parent=n2)
n6 = Node('Rimmicu Vilcea', parent=n2)
n7 = Node('Fagaras', parent=n2)
n8 = Node('Lugoj', parent=n3)
n9 = Node('Craiova', parent=n6)
n10 = Node('Pitesti', parent=n6)
n11 = Node('Bucharest', parent=n7)
n12 = Node('Mehadia', parent=n8)

n1.append_child([n2, n3, n4])
n2.append_child([n5, n6, n7])
n3.append_child([n8])
n6.append_child([n9, n10])
n7.append_child([n11])
n8.append_child([n12])
