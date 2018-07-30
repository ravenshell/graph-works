import Queue as q

class BFS:

    _origin_adjacent_set = None
    _queue = q.Queue()
    _holder = {}
    _origin = None
    _terminus = None
    _weight_type = "same"

    _queue_pointer = None

    def __init__(self, adjacent_set, origin, terminus, weight_type="same"):

        self._origin_adjacent_set = adjacent_set
        self._origin = origin
        self._terminus = terminus
        self._weight_type = weight_type

    def search_graph(self):

        """ Use vertex as edges in the dictionary"""

        return self.find_simple_path()

    def find_simple_path(self):

        self._queue.put(self._origin)
        flag = False

        if self._terminus in self._holder:
            flag = True

        while not self._queue.empty() and not flag:

            self._queue_pointer = self._queue.get()
            # print(self._queue_pointer)

            for vertex in self._origin_adjacent_set[self._queue_pointer]:

                    if not vertex in self._holder:
                        self._queue.put(vertex)
                        print(self._queue_pointer)
                        # print(self._origin_adjacent_set[vertex])
                        self._holder[vertex] = self._queue_pointer

        return self


    def reveal_path(self):

        current_path = []

        if self._terminus in self._holder:
            # create a temporary list holding the terminus
            current_path = [self._terminus]
            # create a temporary terminus
            terminus = self._terminus

            # loop until you get to origin
            while terminus != self._origin:

                terminus = self._holder[terminus]

                # add vertex to to the front of the list while transversing
                current_path = [terminus] + current_path

            return current_path




















set = {
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
bfs = BFS(set, "ATL", "LAX")

path = bfs\
    .search_graph()\
    .reveal_path()

print(path)
