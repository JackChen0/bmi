weight = input('What is your weight? ')
height = input('How tall you are? ')
weight = int(weight)
height = int(height)
height = height / 100
bmi = weight / (height * height)
print('Your BMI is', int(bmi))
if bmi < 18.5:
	print('You are too thin.')
elif bmi >= 18.5 and bmi < 24:
	print('You are perfect.')
elif bmi >= 24 and bmi < 27:
	print('You are a little fat.')
elif bmi >= 27 and bmi < 30:
	print('You are heavy.')
elif bmi >= 30 and bmi < 35:
	print('You are overheavy')
else:
	print('You are endanger')