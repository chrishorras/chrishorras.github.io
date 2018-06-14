# README:
#  * Edit this file where noted to complete exercises.
#  * DO NOT change function names or your code will not pass test cases.
#  * Output must match the reference solution's output EXACTLY, examples of
#    reference solution output will be provided throughout the document.

# Exercise 2-6
# PROMPT(S) (Example user input of '100'):
'''
Enter the amount of the purchase: 100
'''
# OUTPUT:
'''
Purchase Amount: 100.00
State Tax: 5.00
County Tax: 2.50
Total Tax: 7.50
Sale Total: 107.50
'''
def sales_tax():
    # your code here
    #Variable Declarations   
    purchase = 0.0
    stateTax = 0.0
    countyTax = 0.0
    totalTax = 0.0
    totalSale = 0.0
    #Constants for state and county tax rates
    State_Tax_Rate = 0.05
    County_Tax_Rate = 0.025
    #Get the amount of the purchase
    purchase = float(input("Enter the amount of the purchase: "))
    #Calculate state and county sales tax
    stateTax = purchase * State_Tax_Rate
    countyTax = purchase * County_Tax_Rate
    #Calculate total tax and total sale price
    totalTax = stateTax + countyTax
    totalSale = purchase + totalTax
    #Display total sale price
    print("Purchase Amount: ", (purchase))
    print("State Tax: ", (stateTax))
    print("County Tax: ", (countyTax))
    print("Total Tax: ", (totalTax))
    print("Sale Total: ", (totalSale))
# Exercise 2-14
# PROMPT(S) (Example user input of '100', '5', '12', and '10'):
'''
Enter the starting principal: 100
Enter the annual interest rate: 5
How many times per year is the interest compounded? 12
For how many years will the account earn interest? 10
'''
# OUTPUT:
'''
At the end of 10 years you will have $ 164.70
'''
def compound_interest():
	# your code here
	#Variable Declarations
	principal = 0.0
	interest_rate = 0.0
	number_of_compounds = 0.0
	number_of_years = 0.0
	future_amount = 0.0
	#Get the amount of principal orignially deposited
	principal = float(input("Enter the starting principal: "))
	#Get the annual interest rate paid by the account
	interest_rate = float(input("Enter the annual interest rate: "))
	#Get number of times per year interest is compounded
	number_of_compounds = float(input("How many times per year is the interest compounded? "))
	#Get number of years left to earn interest
	number_of_years = float(input("For how many years will the account earn interest? "))
	#Caculate amount of money in account after specified number of years
	future_amount = principal * ((1 + interest_rate / (100 * number_of_compounds))
	 ** (number_of_compounds * number_of_years)) 
	#Display amount of money in the account after the specified number of years
	print("At the end of 10 years you will have $", (round(future_amount,2)))

# Exercise 3-10
# PROMPT(S) (Example user input of '100', '5', '10', and '4'):
	'''
Enter the number of pennies: 100
Enter the number of nickels: 5
Enter the number of dimes: 10
Enter the number of quarters: 4
	'''
# OUTPUT (Less than one dollar):
'''
Sorry, the amount you entered was less than one dollar.
'''
# OUTPUT (More than one dollar):
'''
Sorry, the amount you entered was more than one dollar.
'''
# OUTPUT (Exactly one dollar):
'''
Congratulations!
The amount you entered was exactly one dollar!
You win the game!
'''
def dollar_game():
	# your code here
	#Variable Declarations
	Sum = 0.0
	Quarters = 0
	Dimes = 0
	Nickels = 0
	Pennies = 0
	Correct_Answer = 100
	#Get number of coins guessed
	Pennies = int(input("Enter the number of pennies: "))
	Nickels = int(input("Enter the number of nickels: "))
	Dimes = int(input("Enter the number of dimes: "))
	Quarters = int(input("Enter the number of quarters: "))
	#Calculate sum of guess
	Sum = 25 * Quarters + 10 * Dimes + 5 * Nickels + Pennies
	#Display result of guess
	if Sum == Correct_Answer:
		print("Congratulations!")
		print("The amount you entered was exactly one dollar!")
		print("You win the game!")
	elif Sum < Correct_Answer:
		print("Sorry, the amount you entered was less than one dollar.")
	else:
		print("Sorry, the amount you entered was more than one dollar.")

# Exercise 3-12
# PROMPT(S) (Example user input of '10'):
	'''
Enter the number of packages purchased: 10
	'''
# OUTPUT:
'''
Discount Amount: $ 99.00
Total Amount: $ 891.00
'''
def quantity_discount():
	# your code here
	#Variable Declarations
	Packages = 0.00
	Package_Cost = 0.00
	discount = 0.00
	Discount_Package_Cost = 0.00
	discount_amount = 0.00
	#Get number of packages purchased
	Packages = int(input("Enter the number of packages purchased: "))
	#Calculate cost of packages purchased
	Package_Cost = Packages * 99
	#Determine and display discount
	if Packages <10:
	    print("The number of packages purchased does not offer a discount")
	    discount = 0.00
	elif Packages <=20:
	    discount = 0.10
	elif Packages <=49:
	    discount = 0.20
	elif Packages <=99:
	    discount = 0.30
	else:
	    discount = 0.40
	#Calculate discount amount
	discount_amount = Package_Cost * discount
	#Calculate discounted package cost
	Discount_Package_Cost = Package_Cost * (1-discount)
	#Display discount amount
	print("Discount Amount: $" , (discount_amount))
	#Display discounted package cost
	print("Total Amount: $" , (Discount_Package_Cost))

# Exercise 3-13
# PROMPT(S) (Example user input of '10'):
	'''
Enter the weight of the package: 10
	'''
# OUTPUT:
'''
Shipping charge: $ 4.00
'''
def shipping_charge():
	# your code here
	#Variable Declarations
	Weight = 0.0
	Rate = 0.00
	shipping_charge = 0.0
	#Get weight of package shipped
	Weight = float(input("Enter the weight of the package: "))
	#Determine rate per pound
	if Weight <= 2.0:
		Rate = 1.50
	elif Weight <= 6.0:
		Rate = 3.00
	elif Weight <= 10.0:
		Rate = 4.00
	else:
		Rate = 4.75
	#Calculate shipping charge
	shipping_charge = Weight * Rate
	#Display the shipping charge
	print("Shipping charge: $" , shipping_charge)

# Exercise 4-3
# PROMPT(S) (Example user input of '10', '5', and '0'):
	'''
Enter amount budgeted for the month: 10
Enter an amount spent(0 to quit): 5
Enter an amount spent(0 to quit): 0
	'''
# OUTPUT (Under budget):
'''
Budgeted: $ 10.00
Spent: $ 5.00
You are $ 5.00 under budget. WELL DONE!
'''
# OUTPUT (Matching budget):
'''
Budgeted: $ 10.00
Spent: $ 10.00
Spending matches budget. GOOD PLANNING!
'''
# OUTPUT (Over budget):
'''
Budgeted: $ 10.00
Spent: $ 15.00
You are $ 5.00 over budget. PLAN BETTER NEXT TIME!
'''
def budget_analysis():
	# your code here
	#Variable Declarations
	budget = 0.0
	expenses = 0.0
	total_expenses = 0.0
	more_expenses = "y"
	budget_accuracy = 0.0
	#Get amount budgeted for a month
	budget = float(input("Enter amount budgeted for the month: "))
	#Determine the amount of expenses
	while more_expenses == "y":
		expenses = float(input("Enter an amount spent(0 to quit): "))
		total_expenses += expenses
		more_expenses = input("Would you like to add another expense? y/n: ")
	#Determine budget accuracy
	budget_accuracy = float(budget - total_expenses)
	#Display budget accuracy
	if budget_accuracy == 0:
		print("Budgeted: $" , budget)
		print("Spent: $" , total_expenses)
		print("Spending matches budget. GOOD PLANNING!")
	elif budget_accuracy >= 0:
		print("Budgeted: $" , budget)
		print("Spent: $", total_expenses)
		print("You are $" , budget_accuracy , "under budget. WELL DONE!")
	else:
		print("Budgeted: $" , budget)
		print("Spent: $", total_expenses)
		print("You are $" , abs(budget_accuracy) , "over budget. PLAN BETTER NEXT TIME!")

# Exercise 4-5
# PROMPT(S) (Example user input of '1', '1', '2', '3', '4', '5', '6', '7',
# 	'8', '9', '10', '11', '12'):
	'''
Enter the number of years: 1
For year  1 :
Enter the rainfall amount for the month: 1
Enter the rainfall amount for the month: 2
Enter the rainfall amount for the month: 3
Enter the rainfall amount for the month: 4
Enter the rainfall amount for the month: 5
Enter the rainfall amount for the month: 6
Enter the rainfall amount for the month: 7
Enter the rainfall amount for the month: 8
Enter the rainfall amount for the month: 9
Enter the rainfall amount for the month: 10
Enter the rainfall amount for the month: 11
Enter the rainfall amount for the month: 12
	'''
# OUTPUT:
'''
For  12 months
Total rainfall:  78.00 inches
Average monthly rainfall:  6.50 inches
'''
def average_rainfall():
	# your code here
	#Variable Declarations
	years = 0
	rainfall = 0.0
	total_rainfall = 0.0
	average_rainfall = 0.0
	months = 0
	#Get number of years of data collection
	years = int(input("Enter the number of years: "))
	#Get rainfall for each month
	for year in range(1 , years + 1):
		print("For year " , year , ":")
		for j in range(1, 13):
			rainfall = float(input("Enter the rainfall amount for the month: "))
			total_rainfall += rainfall
	#Calculate total months
	months = 12 * years
	#Calculate average rainfall
	average_rainfall = total_rainfall / months
	#Display months, total inches, and average inches
	print("For " , months , "months")
	print("Total rainfall: " , total_rainfall, "inches")
	print("Average monthly rainfall: " , average_rainfall , "inches")

	# Exercise 4-12
# PROMPT(S) (Example user input of '10'):
	'''
Enter a nonnegative integer: 10
	'''
# OUTPUT:
'''
The factoral of 10 is 3628800
'''
def factorial():
	# your code here
	#Variable Declaratoins
	integer = 0
	factorial = 1

	#Get nonnegative integer
	integer = int(input("Enter a nonnegative integer: "))
	if integer <0:
		print("DO WHAT YOUR TOLD")
		factorial = ""
	#Determine multiplication
	for integer in range (1, integer + 1) :
		factorial = integer * factorial
	print("The factorial of" , integer, "is" , factorial)

# Exercise 4-12
# PROMPT(S) (Example user input of 'python'):
	'''
Enter the string to be converted to Morse code: python
	'''
# OUTPUT:
'''
--.-,--..,..-,..,.--.,---,
'''
def morse_code():
	# your code here
	#Dictionary creation
	morse_dictionary = {" ": " ", ",": "--..--", ".": ".-.-.-", "?": "..--..",
	"0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
	"5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
	"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
	"G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
	"M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
	"S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
	"Y": "-.-", "Z": "--.."} 
	#Get a string to translate
	morse_string = str(input("Enter a string to be converted to Morse code: "))
	#Uppercase all letters
	morse_string = morse_string.upper()
	#Translate into Morse code and display
	for ch in (morse_string):
		print(morse_dictionary[ch] + ",", end = "")
		
# *** DO NOT EDIT BELOW THIS POINT ***
# This part of the file is for testing purposes.
# Your code WILL FAIL the test cases if this is edited.
def main():
	# run each exercise
	sales_tax()
	compound_interest()
	dollar_game()
	quantity_discount()
	shipping_charge()
	budget_analysis()
	average_rainfall()
	factorial()
	morse_code()

if __name__=="__main__":
	main()