import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        # object related to the graph
        self._graph = nx.DiGraph
        # all the nodes of the graph (in this graph
        # nodes are nations, so they are object of type nation)
        self._nodes = None
        self._id_nations = None


    def create_graph(self):
        pass

