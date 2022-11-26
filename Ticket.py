#Ticketing 
print("Welcome to the rollercoaster!")
height=int(input("What is your height in cm? "))
bill=0
if height>120:
    print("Can Ride")
    age=int(input("What is your age? "))
    if age>=18:
        bill=12
        print(f"Tickets are ${bill}")
    elif age<12:
        bill=5
        print(f"Tickets are ${bill}")
    else:
        bill=7
        print(f"Tickets are ${bill}")

    pic=input("Want photo? Yes or No ")
    if pic== "Yes":
        bill=bill+3

    print(f"Total bill is ${bill}")
else:
    print("Can't ride")
    
    
