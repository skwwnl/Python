print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

com = name1 + name2
lo_com = com.lower()

t = lo_com.count("t")
r = lo_com.count("r")
u = lo_com.count("u")
e = lo_com.count("e")

to_1 = t + r + u + e

l = lo_com.count("l")
o = lo_com.count("o")
v = lo_com.count("v")
e = lo_com.count("e")

to_2 = l + o + v + e

to_str = str(to_1) + str(to_2)
to = int(to_str)
if to < 10 and to > 90:
    print(f"Your score is {to}, you go together like coke and mentos.")
if to > 40 and to < 50:
    print(f"Your score is {to}, you are alright together.")
else:
    print(f"Your score is {to}.")

