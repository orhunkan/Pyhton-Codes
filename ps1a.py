total_cost =float(input("Price of the dream house"))
portion_down_payment =0.25
current_savings=float(0)
down_payment=total_cost*portion_down_payment
r=0.04
annual_salary =float(input("Amount of the annual salary"))
portion_saved=float(input("Percentage of the saving from annual salary"))
numberofmonths=0
while current_savings<down_payment:
    current_savings+=((annual_salary/12)*portion_saved)+((current_savings*r)/12)
    numberofmonths+=1
print("Months for saving up down payment",numberofmonths)