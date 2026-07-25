# # print("Hello ketan")
# # print("Test")
# #
# # #Ask the user name
# # user_name = input("What is your name? ")
# # #Ask the user age
# # user_age = input("what is your age?")
# # #Print combine all the stuff
# # print("Hello " + user_name + ",you are" + user_age)
# #-------------------------------------------------------------
#
# #Functions
#
# # def say_hello():
# #     print("Hello")
# #     print("test")
# #     print("ketankulkarni")
# #
# #
# # say_hello()
# # say_hello()
# # say_hello()
# #-------------------------------------------------------------
#
# # def say_hello(user_name,user_age):
# #     print("Hello " + user_name + "you are " + str(user_age))
# #
# # def double_number(number):
# #     result = number * 2
# #     return result
# #
# # def print_double_number(number):
# #     result = double_number(number)
# #     print(result)
#
# # print(double_number(4))
# # print(double_number(3))
# # print(result)
# #
# # a = 2
#
# # say_hello("Ketan", 34)
# # say_hello("Kunal",30)
# # say_hello("Jyoti",60)
# # say_hello("Deepak",65)
# ##############################################################
#
# # def user_profile(user_name,user_age):
# #     print("Hello "+ user_name +", your age is "+ str(user_age))
#
# # user_profile("Ketan", 34)
#
# # def sum_of_numbers(number1, number2):
# #     return number1 + number2
# #
# #
# # print(sum_of_numbers(3, 5))
#
# def avg_list():
#     number_list = [1.0,4.5,7.8,8.6]
#     average = sum(number_list)/len(number_list)
#     print(average)
#
# avg_list()

def temperature_converter(current_temp):
    #print("Enter the temperature in Celsius: ")
    f = current_temp * 1.8 + 32
    return f
print(temperature_converter(47))