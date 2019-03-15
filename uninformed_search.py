"""
dfs ids for map exploration
"""
# import pandas as pd
#
# df = pd.read_csv('input.csv')
# city_names = df.columns
# print(city_names)
#
# city_distance = df.iloc[1:, 1:]
# print(city_distance)
import ids_search
import dfs_search
import generate_state_space_tree


class Node:
    def __init__(self, city_name, parent, id):
        self.city_name = city_name
        self.parent = parent
        self.child = []
        self.id = id
        # id can be used for printing sequence of nodes visited. For eg n1 will
        # have id 1, n2 will have id 2

    def __repr__(self):
        # return str(self.id)+self.city_name
        child_names = [x.city_name for x in self.child]
        return "City Name: {}, Parent: {}, Child: {}".format(self.city_name, self.parent, child_names)

    def __str__(self):
        return str(self.id)+'-'+self.city_name

    def append_child(self, children):
        for child in children:
            self.child.append(child)


n1 = Node('Arad', None, 1)
n2 = Node('Sibiu', n1, 2)
n3 = Node('Timisoara', n1, 3)
n4 = Node('Zerind', n1, 4)
n5 = Node('Oradia', n2, 5)
n6 = Node('Rimmicu Vilcea', n2, 6)
n7 = Node('Fagaras', n2, 7)
n8 = Node('Lugoj', n3, 8)
n9 = Node('Craiova', n6, 9)
n10 = Node('Pitesti', n6, 10)
n11 = Node('Bucharest', n7, 11)
n12 = Node('Mehadia', n8, 12)

n1.append_child([n2, n3, n4])
n2.append_child([n5, n6, n7])
n3.append_child([n8])
n6.append_child([n9, n10])
n7.append_child([n11])
n8.append_child([n12])

generate_state_space_tree.generate_tree(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12)

print("\nIDS")
if not ids_search.ids(n1, 'Bucharest', 4):
    print('Goal state not found')

print("\nDFS")
dfs_search.dfs_main(n1, 'Bucharest')
