year = int(input("Enter year: "))

if year % 400 == 0:
    print("cabise Year")
elif year % 100 == 0:
    print("Not cabise Year")
elif year % 4 == 0:
    print("cabise Year")
else:
    print("Not cabise Year")
