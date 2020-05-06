print("Calculate your Percentage!")

phy=float(input("Enter your physics Marks"))
chem=float(input("Enter your chemistry Marks"))
maths=float(input("Enter your maths Marks"))
eng=float(input("Enter your english Marks"))
ip=float(input("Enter your IP Marks"))


Total=phy+chem+maths+eng+ip

result=(Total/500*100)
print("Percentage",result)
