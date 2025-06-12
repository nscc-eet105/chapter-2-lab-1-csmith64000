print("Chris Smith")
print("Ch.2 Lab 1")
print("06/11/2025")
First_name= (input("Enter your first name:"))
Last_name =(input("Enter your last name:"))
Ammount = int(input("Ammont of marbles to purchase:"))

print("Your order is ready",First_name,Last_name)
print(Ammount,("Marbles"),("@"),(f"${1.20:.2f}"))

print(("Total cost is"),(f"${Ammount*1.20:.2f}"))
