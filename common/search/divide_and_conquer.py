class DividerAndConquer:

    def __init__(self):

        return


    def find_max_crossing_sub_array(self, data, low, mid, high):

        left_sum = 0
        right_sum = 0
        left_max_index = 0
        right_max_index = 0

        left_max = -100000000000000000
        right_max = -100000000000000000



        for index in range(mid):
            left_sum = left_sum + data[index]
            # print(left_sum, left_max)
            if left_sum > left_max:
                left_max = left_sum
                left_max_index = index + 1

        for _index in range(mid, high):
            right_sum = right_sum + data[_index]
            # print(right_sum, right_max)
            if right_sum > right_max:
                right_max = right_sum
                right_max_index = _index + 1

        #       index               index           max
        return left_max_index, right_max_index, (right_max + left_max)


    def find_max_subarray(self, data, low, high):

        if low == high or (high - low) == 1:
            # print(data[low])
            return low, high, data[low]
        else:
            mid = (low + high) / 2
            # print indexes for low, mid, and high
            print(low, mid, high)
            left_low, left_high, left_max = self.find_max_subarray(data, low, mid)
            right_low, right_high, right_max = self.find_max_subarray(data, mid, high)
            cross_low, cross_high, cross_max = self.find_max_crossing_sub_array(data, low, mid, high)

            print("Main: ",left_max, right_max, cross_max)

            if (left_max > right_max and left_max > cross_max):
                return left_low, left_high, left_max
            elif (right_max > left_max and right_max > cross_max):
                return right_low, right_high, right_max
            elif (cross_max > left_max and cross_max > right_max):
                return cross_low, cross_high, cross_max



data = [5, 6, -7, 8, -8, 88, 10]

dnc = DividerAndConquer()

# fix recursion issue add data to function

# print(dnc.find_max_crossing_sub_array())
dnc.find_max_subarray(data, 0, len(data))
