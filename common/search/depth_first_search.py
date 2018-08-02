import Queue as q

class DFS:

    _origin = None;
    _terminus = None;
    _graph = None;

    _transverse_list = []

    _stack = []

    _predecessor_tree = {}

    def __init__(self, graph, origin, terminus):

        self._origin = origin
        self._terminus = terminus
        self._graph = graph
        return

    def find_path(self):

            for vertex in self._graph[self._origin]:

                result = self.transverse_path(vertex)

                self.clear_temps()

                self.check_result(result, vertex)



    def transverse_path(self, vertex):

        if vertex in self._graph:
            for predecessor in self._graph[vertex]:
                if predecessor == self._terminus:
                    return self._stack
                else:
                    self.check_path(predecessor)

        return 0

    def check_result(self, result, vertex):

        if result == 0:
            do_nothing = 0
            # print("could not find a path to terminus at vertex: ", vertex)
        else:
            print("found path at vertex: ", vertex)

            for vertex in result:
                print("vertex: ", vertex)

    def clear_temps(self):
        self._transverse_list = []
        self._stack = []

    def check_path(self, predecessor):

        if predecessor in self._graph:
            if predecessor not in self._transverse_list:
                self._transverse_list.append(predecessor)
                self._stack = self._stack + [predecessor]
                self.transverse_path(predecessor)




graph = {
"ATL": {"MIA", "DCA", "ORD", "MCI", "DFW", "DEN"},
"MIA": {"LGA", "DCA", "ATL", "DFW"},
"DFW": {"LAX", "DEN", "MCI", "ORD", "ATL", "MIA"},
"LAX": {"SFO", "DEN", "MCI", "DFW"},
"DEN": {"SFO", "LAX", "MCI", "DFW", "SEA", "ATL"},
"SEA": {"SFO", "DEN", "ORD", "LGA"},
"MCI": {"DEN", "LAX", "DFW", "ATL", "ORD", "LGA"},
"ORD": {"SEA", "MCI", "DFW", "ATL", "DCA", "LGA"},
"DCA": {"ORD", "ATL", "MIA", "LGA"},
"LGA": {"SEA", "MCI", "ORD", "DCA", "MIA"},
"SFO": {"SEA", "DEN", "LAX"}
}
dfs = DFS(graph, "ATL", "LAX")

dfs.find_path()
