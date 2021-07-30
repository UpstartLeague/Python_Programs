# Python program to check whether a number is Prime or not
print("To check whether a number is Prime or not")
num = int(input("Enter a number: "))

# checking if the entered number is prime number
# all prime numbers are greater than 1
if num > 1:
    for i in range(2, num):
        if (num % i == 0):
            print(num, "is not a Prime number.")
            break
    else:
        print(num, "is a Prime number.")