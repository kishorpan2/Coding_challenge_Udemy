
'Create a python program to calculate price of Pizza based on size topping '
print('Thank you for choosing Python Pizza')
bill = 0
size=input("What size pizza do you want ? Please enter S for small, M for medium and L for large: ")
if size == "S":
    bill=15
elif size== "M":
    bill=20
else:
    bill =25
add_pepporoni =input("Do you want Pepperoni? Please enter Y for Yes  or N for No: ")
if add_pepporoni =="Y":
    bill +=3
extra_cheese=input("Do you want Extra cheese? Please enter Y for Yes  or N for No: ")
if extra_cheese =="Y":
    bill +=1
print(f"Your final bill is {bill}")
