monthly_expenses=[2200,2350,2600,2130,2190]

#jan,feb,mar,apr,may

#expenses in feb more than jan ?

print(monthly_expenses[1]-monthly_expenses[0])

#Find out your total expense in first quarter (first three months) of the year.

annual=12 
quarter=(annual)//4 

print(sum(monthly_expenses[:quarter]))

#Find out if you spent exactly 2000 dollars in any month

if 2000 in monthly_expenses:
    print("True")
else:
    print("False")
    
    
#June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
    
#june=1980 
    
monthly_expenses.append(1980)
print(monthly_expenses)

# You returned an item that you bought in a month of April and
#got a refund of 200$. Make a correction to your monthly expense list
#based on this

monthly_expenses[3]=monthly_expenses[3]-200
print(monthly_expenses)
