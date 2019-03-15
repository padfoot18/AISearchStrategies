import pandas as pd
import numpy as np

df = pd.read_csv('input.csv')

city_distance = df.iloc[1:, 1:]
city_distance = np.array(city_distance)

heuristics = {'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Dobreta': 242, 'Eforie': 161, 'Fagaras': 176,
              'Guirgui': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt':234, 'Oradia': 380,
              'Pitesti': 10, 'Rimmicu Vilcea': 193, 'Sibiu': 253, 'Timisora': 329, 'Urziceni': 80, 'Vaslui': 199,
              'Zerind': 374}


class Node:
    def __init__(self, city_name, parent, id, level):
        self.city_name = city_name
        self.level = level
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
