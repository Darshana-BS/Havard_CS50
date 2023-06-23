# total_cost = float(input('Total cost of the house without the extra charges: '))
# extra_charges = float(input('Enter the Extra charges: '))

#extra charges distribution amount
Raw_price = 3800000
Stamp_Duty = 237700
Mhada_Transfer = 15000
Society_Transfer =25000
Society_other = 10000
Advocate = 75000
braokerage = 50000

extra_charges = int(Stamp_Duty+Mhada_Transfer+ Society_Transfer + Society_other + Advocate + braokerage)
Total_amount_to_be_paid =  int(Raw_price+extra_charges)
print("Total amount : ", f"{Total_amount_to_be_paid:,}")

#amount paid
loan = 1800000
Raw_price = 3800000-51000-750000
Stamp_Duty = 237700-237700
Mhada_Transfer = 15000
Society_Transfer =25000
Society_other = 10000-10000
Advocate = 75000-75000
braokerage = 50000

extra_charges_paid_done = int(Stamp_Duty+Mhada_Transfer+ Society_Transfer + Society_other + Advocate + braokerage)
Total_amount_to_be_remaining_to_be_paid =  int(Raw_price+extra_charges_paid_done)
print("Amount paid : " , (f"{Total_amount_to_be_paid-Total_amount_to_be_remaining_to_be_paid:,}"))
print("Amount remaining : ", f"{Total_amount_to_be_remaining_to_be_paid:,}")

#loadn amount
loan = 1800000
loan_fees = 3500
dad = 800000
Raw_price1 = 1200000

#current_balance
current_balance = 517495
print('current_balance', f"{current_balance:,}")
current_balance_new = current_balance + dad
current_balance_after_payment = current_balance_new - Raw_price1
To_be_collected_amount = 100000 + 5000
print('Balance after payament done : ', f"{(current_balance_after_payment+To_be_collected_amount):,}")
