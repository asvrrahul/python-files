import random
while True:
	i=input("press 'r' to roll and 'q' to quit")
	if(i=='r'):
		print("hi!")
		print("the number is",random.randint(1,6))

	else:
		print("next!")
		exit()