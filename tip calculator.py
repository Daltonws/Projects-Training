print("Welcome to the tip caclulator!")
bill = float(input("What is your total bill? $ "))
tip_entered = int(input("How much tip would you like to give in percentage? 10, 15, 20? "))
people = int(input("How many people to split the bill? "))
tip_percent = float(tip_entered / 100) 
total_bill = (bill * tip_percent + bill) 
bill_per_person = float(total_bill / people)
# final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"The total for each person is ${final_amount}")
