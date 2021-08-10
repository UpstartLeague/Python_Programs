number= int(input("Enter a number: "))
sum = 0
while num>0:
   digit = num % 10
   sum += digit ** 3
   num //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
