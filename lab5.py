from operator import index
from data import Time, Point
import math
# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
def time_add(time1:Time, time2:Time):
    sum_seconds = time1.second + time2.second
    sum_minutes = time1.minute + time2.minute + sum_seconds//60
    sum_hours = time1.hour + time2.hour + sum_minutes//60

    hour = sum_hours
    minute = sum_minutes % 60
    second = sum_seconds % 60

    return hour, minute, second
#The purpose of this function is to take in two times with hours, minutes, and seconds and return the sum of both times without seconds or minutes being greater than 60.
#This function take an input of two times of class Time containing hours, minutes, and seconds. Then it adds the seconds, minutes, and hours. The whole number produced when dividing byn 60 gets added to minutes or hours with the modulus saving the remainder which is displayed in the output.
#def time_add(time1:Time, time2:Time):
#Refer to lab5_tests.py/data_tests.py for tests

# Part 4
def is_descending(values:list[int]):
    for i in range(1,len(values)):
        if values[i] > values[i-1]:
            return False
    return True
#The purpose of this function is to take in a list of integers and return True only if its in descending order.
#The input here is a list of integers and the output is a boolean that is either True or False. The function checks each value of the lsit from 1 to the last element checking if the value at i is greater than the previous.
#def is_descending(values:list[int]):
#Refer to lab5_tests.py/data_tests.py for tests


# Part 5
def largest_between(values:list[int], lower:int, upper:int):
    if lower > upper:
        return None
    lower = max(0,lower)
    upper = min(len(values)-1,upper)
    index = lower

    for i in range(lower, upper+1):
        if values[i] > values[lower]:
            index =  i
    return index
#The purpose of this function is to return the index of the largest value in the list that is between the two indices of lower and upper (bounds).
#The input is a list of values, an upper bound, and a lower bound. The function first checks if the lower bound is greater than the upper and then adjusts the bounds to be within bounds if they aren't already. Only then does the for loop process and finally returns the output, index value.
#def largest_between(values:list[int], lower:int, upper:int):
#Refer to lab5_tests.py/data_tests.py for tests


# Part 6
def furthest_from_origin(values: list[Point]):
    greatest_distance = 0
    greatest_index = 0

    if not values:
        return None
    for i in range(len(values)):
        point = values[i]
        distance = math.sqrt(point.x**2 + point.y**2)

        if distance > greatest_distance:
            greatest_distance = distance
            greatest_index = i

    return greatest_index
#The purpose of this function is to