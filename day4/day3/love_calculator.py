print("Welcome to Love Calculator")
name1 = input("What is your name? ")
name2 = input("What is their name? ")
name1 = str(name1)
name2 = str(name2)

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

t = lower_case_name1.count("t")
r = lower_case_name1.count("r")
u = lower_case_name1.count("u")
e = lower_case_name1.count("e")
l = lower_case_name1.count("l")
o = lower_case_name1.count("o")
v = lower_case_name1.count("v")
e = lower_case_name1.count("e")

T = lower_case_name2.count("t")
R = lower_case_name2.count("r")
U = lower_case_name2.count("u")
E = lower_case_name2.count("e")
L = lower_case_name2.count("l")
O = lower_case_name2.count("o")
V = lower_case_name2.count("v")
E = lower_case_name2.count("e")

true = int((t+T) + (R+r) + (u+U) + (e+E))
love = int((l+L) + (o+O) + (v+V) + (e+E))
love_score = str(true) + str(love)

if love_score > "90" or love_score < "10" :
	print(f"Your score is,", love_score, "you go together like coke and mentos")

elif love_score > "40" and love_score < "50" :
	print(f"Your score is,", love_score, "you are alright together.")

else :
	print(love_score)
