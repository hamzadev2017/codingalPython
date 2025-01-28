

#Input a word or sentence

string = input("Please enter your own String : ")

string1 = ('')

#loop for printing in reverse

for i in string:

  string1 = i + string1

print("\nThe Original String = ", string)

print("The Reversed String = ", string1)
