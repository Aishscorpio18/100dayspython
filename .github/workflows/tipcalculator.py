print("Welcome to the tip calculator!")
total_bill=input("What was the total bill?")
#can change type in input function itself.
tip=input("How much tip would you like to give? 10,12 or 15?")
split_bill=(input("How many people to split the bill?"))
tip=int(tip)
total_bill=float(total_bill)
split_bill=float(split_bill)
#print(type(total_bill))
#print(type(split_bill))
each_bill=total_bill/split_bill*(1+tip/100)
each_bill=round(each_bill,2)
print(f"Each person should pay: {each_bill}")
