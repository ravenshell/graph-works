class InsertionSort:


    def __init__(self, data):
        self.data = data
        self



    def sort(self):

        for j in range(1, len(self.data)):
            key = self.data[j]
            i = j - 1

            while i > -1 and self.data[i] > key:
                """
                paste value to index data[i+1] break the loop 
                when our index is out of bound or data[i] is 
                lower or equal to key
                """
                self.data[i + 1] = self.data[i]
                print(self.data)
                i  = i - 1
            self.data[i + 1] = key

        return self.data


    def recurse(self, val):

        if val == 0:
            return 0
        else:
            decrement = val - 1
            print("->",decrement)
            count = self.recurse(decrement)
            print("<-", count)
            return count




# data = [3,5, 1, 4, 6]
data = [6,5,4,3,2,1]
ins = InsertionSort(data)
# print(ins.sort())

digit = 8
index = 1
holder = []
while digit > 0 :
    digit = digit - 1
    holder.append((index, digit))
    index = index + 1
    print(holder)

# Simple recursion test
# ins.recurse(10)