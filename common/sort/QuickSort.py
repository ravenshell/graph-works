class QuickSort:


    def partition(self, data, start, end):

        key = data[end]
        i = start - 1

        for index in range(start, end):
            print(index)
            if data[index] <= key:
                i = i + 1
                temp = data[i]
                data[i] = data[index]
                data[index] = temp
                print('inner-loop: ', i, data)
        temp = data[i + 1]
        data[i + 1] = data[end]
        data[end] = temp

        print(i + 1, data)


"""
 CASE 1 
 The data below has as its pivot point as a value
 smaller than all value on the left sub-array[0, 2]
 breaking the partition
 data = [ 3, 5, 9, 4, 1, 2] 
"""
data = [ 3, 5, 9, 4, 1, 2]
qs = QuickSort()
qs.partition(data, 0, len(data) - 1)