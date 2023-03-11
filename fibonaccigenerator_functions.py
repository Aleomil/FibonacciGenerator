#Function of Fibonacci number:
def fibonacci(num):
    if num > 1:
        return fibonacci(num-1)+fibonacci(num-2)
    else:
        return num

#Function to determine whether
def isFibo(num,lenghtofFibosequence):
    if num in fiboList(lenghtofFibosequence):
        return True
    else:
        return False

#Function to print the Fibo list given a num
def fiboList(num):
    list=[]
    for i in range(num):
        list.append(fibonacci(i))
    return list

print(fiboList(30))
print(isFibo(3,8))
print(isFibo(121393,30))