# Using a while loop, print all numbers between 1 and 10
i = 1
print("Printing out 1 to 10 with while loop: ")
while i <= 10:
    print(i)
    i += 1
print("**********************")

# Prompt user for start and end numbers to print with while loop:
n = int(input('Please give a starting number: '))
m = int(input('Please give an ending number '))

while n <= m:
    print(n)
    n += 1
print("**********************")

# print out odd numbers between 1 and 10
q = 1
print("Printing out all odd numbers between 1 to 10 with while loop: ")
while q <= 10:
    if (q % 2 != 0):
        print(q)
    q += 1
print("**********************")

# Prompt user for coins, add a coin while string equals "yes", stop loop when string equals "no"
coins = 0
print("You currently have ", coins, " coins.")
prompt = input("Would you like to add a coin? (yes or no) ")
while prompt == "yes":
    coins += 1
    print("You currently have ", coins, " coins.")
    prompt = input("Would you like to add a coin? (yes or no) ")
else:
    print("good bye!")
print("**********************")
