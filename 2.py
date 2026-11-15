age = int(input("Enter your age: "))

if age < 5:
    print("Ticket is free")

elif age < 18:
    print("Ticket price: 50000 Toman")

elif age <= 60:
    print("Ticket price: 100000 Toman")

else:
    print("Ticket price: 70000 Toman")
