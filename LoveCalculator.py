
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


combine_name=name1+name2
lower_case=combine_name.lower()
t=lower_case.count("t")
r=lower_case.count("r")
u=lower_case.count("u")
e=lower_case.count("e")
l=lower_case.count("l")
o=lower_case.count("o")
v=lower_case.count("v")
e=lower_case.count("e")

total1=t+r+u+e
total2=l+o+v+e

j=str(total1)+str(total2)
i=int(j)
print(j)
if i<10 or i>90:
    print(f"Your score is {i}, you go together like coke and mentos.")
elif i>40 and i<50:
    print(f"Your score is {i}, you are alright together.")
else: 
    print(f"Your score is {i}.")


