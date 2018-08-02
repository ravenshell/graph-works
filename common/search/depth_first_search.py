
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
        if vertex == self._terminus:
            return [vertex] + self._stack

        # if vertex is contained as a vertex with
        # predecessors in graph
        if vertex in self._graph:

            # loop through vertex predecessors
            for predecessor in self._graph[vertex]:

                # if predecessor is our terminus
                if predecessor == self._terminus:

                    # add predecessor to the front of stack
                    self._stack = [predecessor] + self._stack
                    # return our stack of paths
                    return self._stack
                else:
                    self.check_path(predecessor)

        return 0

    def check_result(self, result, vertex):

        if result == 0:
            do_nothing = 0
            print("could not find a path to terminus at vertex: ", vertex)
        else:
            print("found path at vertex: ", vertex)
            print(result)

    def clear_temps(self):

        # clear transverse list and stack
        self._transverse_list = []
        self._stack = []

    def check_path(self, predecessor):

        # check if predecessor is in graph
        if predecessor in self._graph:

            # transverse predecessor only if
            # predecessor has not been transversed before
            if predecessor not in self._transverse_list:

                # add predecessor to transverse list
                self._transverse_list.append(predecessor)

                # add predecessor to stack
                if predecessor not in self._stack:
                     self._stack = [predecessor] + self._stack

                # transverse predecessor
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
