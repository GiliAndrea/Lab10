import networkx as nx
from networkx.algorithms.traversal import dfs_tree

from database.DAO import DAO
from model.country import Country


class Model:

    def __init__(self):
        # object related to the graph
        self._graph = nx.Graph()
        self._nodes = []


    def create_graph(self, year: int):
        # creation of the graph
        self._graph.clear()
        self._nodes = []
        # all the nodes of the graph (in this graph
        # nodes are nations, so they are object of type nation)
        self._nodes = DAO.get_all_nodes(year)
        id_map_nations = {}
        for n in self._nodes:
            id_map_nations[n.stato] = n
        # all the nodes are putted in the graph
        self._graph.add_nodes_from(DAO.get_all_nodes(year))
        # all the appropriate edges are putted in the graph
        for e in DAO.get_all_edges(year):
            self._graph.add_edge(id_map_nations[e[0]], id_map_nations[e[1]])

    def get_number_linked_component(self):
        return nx.number_connected_components(self._graph)

    def get_nodes_info(self):
        result = []
        for node in self._graph.nodes():
            result.append([node, self._graph.degree(node)])
        return result

    def get_nodes(self) -> list[Country]:
        return self._nodes

# second part


    # this is the first way to search the country that are reachable from the source
    # is the simplest one
    def search_leaked_country_source(self, country: Country):
        tree = dfs_tree(self._graph, country)
        return tree.nodes()


    # this is the second way to search the country that are reachable from the source
    # is the one that is more difficult than the first version
    def search_leaked_country_source_version_2(self, country: Country):
        # the setting of the variable
        visited_country = []
        unvisited_country = [country]
        present_country = country
        self.recursive_function(present_country = present_country, visited_country = visited_country,
                                unvisited_country = unvisited_country)


    def recursive_function(self, present_country: Country, unvisited_country: list,
                           visited_country: list):
        # terminal condition
        if not unvisited_country:
            return visited_country
        # recursive condition
        else:
            unvisited_country.remove(present_country)
            visited_country.append(present_country)
            neighbors = list(self._graph.neighbors(present_country))
            unvisited_country.append(neighbors)
            for node in neighbors:
                if node not in visited_country:
                    self.recursive_function(present_country = node, unvisited_country = unvisited_country,
                                            visited_country = visited_country)
                else:
                    pass