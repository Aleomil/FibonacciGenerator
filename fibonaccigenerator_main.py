from fibonaccigenerator_functions import *
from genericfunctions import *

#Main programm
print("-----------------------------------------")
print("-----------------WELCOME-----------------")
print("-----------------------------------------")

print("Please select the programm you want to execute")
print("Press 1 in case you want to display the n-fibonacci sequence")
print("Press 2 to check whether a number is in the n-fibonacci sequence")
print("...")

fibo_mode=input(" ")
length_list=2
number_to_check=1


while parse_first_input(fibo_mode):
    length_list=input("Please provide the length of the Fibonacci list[1-30]: ")
    while parse_listlength(int(length_list)):    
        if fibo_mode =="1":
            print(fiboList(int(length_list)))
            break
        elif fibo_mode =="2":
            number_to_check = input("Please enter the number to check")
            while parse_fiboNumber(int(number_to_check)):
                print("....Checking.....")
                print("...")
                if isFibo(int(number_to_check),int(length_list)) and parse_fiboNumber(int(number_to_check)):
                    print("The number",number_to_check,"is in the list!")
                    print(fiboList(int(length_list)))
                    break
                else:
                    print("The number is not in the list")
                    break
            else:
                number_to_check=input("Please provide a number or press ENTER/SPACE to exit the programm:")
    else:
        length_list=input("Please provide a number between 1 and 30")
else:
        if fibo_mode =="" or length_list=="" or number_to_check=="":
            exit