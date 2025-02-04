a = int(input("write numbers : "))
numdigit = 0
while a > 0:
    numdigit += 1
    a = a // 10
    
print("The number of digits in the number are:", numdigit)
