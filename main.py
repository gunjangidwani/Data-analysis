# string = 'Hello World'
# integer = 4
# float_ = int(3.99)
# boolean = True
# operation = int("2") - 2
# print(string.split('e'), type(string))
# print(oct(integer), type(integer))
# print(float_, type(float_))
# print(boolean, type(boolean))
# print(operation, type(operation))

# x = 7
#
# if x >2:
#     print("X is bigger")
# elif x > 0:
#     print("X is bigger than zero")
# else:
#     print("X is smaller")

# lst = [ 2, 3, 4, 5, 1, 6, 7, 1, 9, 10]
# copy_lst = lst[:]
# print(lst.append(11), lst)
# print(set(lst), lst)
# print(lst.append((11)), lst)
#
# print(lst.insert(0,12), lst)
# if not self.is_empty():
#             return self.items.pop()


# def squared(x: int):
#     '''
#
#     :param x: int
#     :return y: int representing the squared value of x
#     '''
#     y = x ** 2
#     return y
#
# # print(squared(10))
# def pow(x: int, y: int):
#     return x ** y
#
# print(pow(3, 2))

# str1 = 'Hello World'
# def reverse(string):
#     return string[::-1]
#
# print(reverse(str1))

# def sum_of_digits(num):
#     result = 0
#     if num >0:
#         str1 = str(num)
#         for i in range(len(str1)):
#             result += int(str1[i])
#         return result
#     else:
#         return 0
#
#
# print(sum_of_digits(125))


# def is_prime(num):
#     # Your code here
#     if num == 0 or num == 1:
#         return False
#     elif num > 1:
# # check for factors
#         for i in range(2, num):
#             if (num % i) == 0:
#                 return False
#         else:
#             return True
#     # if input number is less than
#     # or equal to 1, it is not prime
#     else:
#         return True

# def closest_num(list, num):
#     small=0
#     big=0
#     for i in range(len(list)):
#         if list[i] == num:
#             return i
#         elif list[i] < num & list[i] > small:
#             small = list[i]
#         elif list[i] > num & list[i] > big:
#             big = list[i]
#     return small if num-small < num-big else big

import json
student_data = {"name": "David", "age": 13, "address": "bhopal", "marks": 43}
print(type(student_data))
# data = json.loads(student_data)
# print(type(data), data.get("name"), data.get("age"), data.get("address"))
for i in student_data.items():
    print(type(i))








