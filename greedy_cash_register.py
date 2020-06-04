# Author: Matthew Palomar
# Date: 6/1/20
# https://cs50.harvard.edu/x/2020/weeks/6/
# https://cs50.harvard.edu/x/2020/psets/6/
# https://cs50.harvard.edu/x/2020/psets/6/cash/

while True:
    try:
        dollars = float(input("Change owed: $"))
        cents = round(dollars * 100)
        print("")
    except ValueError:
        print("Not a valid input.\n")
        continue
    if cents == 0 or cents < 0 or type(dollars) is not float:
        print("Enter a valid value.\n")
        continue
    else:
        break

quarters = cents // 25
print(quarters, " quarters, ")
dimes = (cents % 25) // 10
print(dimes, " dimes, ")
nickels = (cents % 25) % 10 // 5
print(nickels, " nickels, ")
pennies = (cents % 25) % 10 % 5
print(pennies, " pennies")

print("")

print("Total coins: ", end="")
print(quarters + dimes + nickels + pennies)
