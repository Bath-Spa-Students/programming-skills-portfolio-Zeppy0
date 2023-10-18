# Define the cost of one USB stick and the total budget
usb_stick_cost= 6 # £6 Each
Total_Budget= 50 # £50 budget

# Calculate the number of USB sticks she can buy
number_of_usb_sticks = Total_Budget // usb_stick_cost 

# Calculate how much miney she is left with 
money_left = Total_Budget % usb_stick_cost 

print(f"She can buy {number_of_usb_sticks} USB Sticks.")
print(f"She will have £{money_left} left.")