def binary_search(list, number):

    lower_number = 0
    end_number = len(list)-1

    while lower_number <= end_number:
        mid_point = lower_number + (end_number-lower_number)//2
        mid_value = list[mid_point]
        if mid_value == number:
            return mid_point

        elif number < mid_value:
            end_number = mid_point-1

        else:
            lower_number = mid_point +1
    return None
list_a=[1,2,3,4,5,6,7,8,9,10,11]
number_a=1


print(binary_search(list_a,number_a))


