import os
def clear():
	os.system('cls')
#Functions with Outputs
clear()

formatted_f_name = str(input("enter your first name: ")).title()
formatted_l_name = str(input("enter your last name: ")).title()
	
def format_name(f_name, l_name):
	print(f"Your name is " + f_name + " " + l_name)
  
format_name(f_name=formatted_f_name, l_name=formatted_l_name)