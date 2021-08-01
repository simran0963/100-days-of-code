print("BMI Calculator")
weight = input("enter your weight in kg ")
weight = float(weight)

height = input("enter your height in m ")
height = float(height)

bmi = weight/(height ** 2)
bmi_as_int = int(bmi)

# print("Your BMI is " + str(result))
# print(bmi_as_int)
print(round(bmi_as_int))