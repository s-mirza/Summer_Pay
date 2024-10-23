'''
Author: <Sarah Mirza>

Program Title: <Summer Pay>

File Description:

<This program calulates your monthly income with and without taxes, your expenses and your expenditure.>

'''
Hourly_rate = input("What is your hourly rate of pay?")
Hourly_rate = float(Hourly_rate)

week_hours = input("How many hours did you work each week?")
week_hours = float(week_hours)

print("*******************************************************************")
print("Information about your Pay")
print("-------------------------------")

Gross_pay = (Hourly_rate * week_hours)*5
print(f"-->Gross Pay:  ${Gross_pay:.2f}")

Taxes_owed = ((Hourly_rate * week_hours)*5)*0.2
print(f"-->Taxes Owed: ${Taxes_owed:.2f}")

Net_pay = Gross_pay - Taxes_owed
print(f"-->Net Pay:    ${Net_pay:.2f}")

print("-------------------------------")
scs = Net_pay * 0.15
print(f"-->School Clothes Savings:            ${scs:.2f}")

sss = Net_pay * 0.03
print(f"-->School Supplies Savings:           ${sss:.2f}")

sb = Net_pay * 0.15
print(f"-->Your Savings Bonds Cost:           ${sb:.2f}")

psb = sb * 0.75
print(f"-->Parent Savings Bonds Contribution: ${psb:.2f}")

print("-------------------------------")
lo = Gross_pay - (Taxes_owed + scs + sss + sb)
print(f"You have ${lo:.2f} left over.")
print("-------------------------------")

