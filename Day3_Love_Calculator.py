# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower1 = name1.lower()
lower2 = name2.lower()

combine = lower1 + " " + lower2

# print(combine)

M = combine.count('m')
O = combine.count('o')
S = combine.count('s')
T = combine.count('t')
total1 = M + O + S + T

# print(total1)

L = combine.count('l')
O = combine.count('o')
V = combine.count('v')
E = combine.count('e')
total2 = L + O + V + E

# print(total2)
love = str(total1) + str(total2)
# love = total1 + total2
# print(love)
# print(type(love))

if int(love) < 10 or int(love) > 90:
  print(f"your score is {love}, you go together like coke and mentos.")
elif int(love) >= 40 and int(love) <= 50:
  print(f"Your score is {love}, you are alright together.")
else:
  print(f"Your score is {love}.")


