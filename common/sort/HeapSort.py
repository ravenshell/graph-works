class HeapSort:

    def __init__(self, heap):
        self.heap = heap

        return


    def max_heap(self):

        return

    def min_heap(self):

        return


    def build_heap(self, heap_type=True):
        """

        :param type: true for maxheap false other wise
        :return:
        """

        heap_size = self.heap.size()

        if heap_type is True:
            for _ in range(heap_size / 2): # decrement backwars
                self.max_heap()
        else:
            for _ in range(heap_size / 2):
                self.max_heap()



    def sort(self):

        return