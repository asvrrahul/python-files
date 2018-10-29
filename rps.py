import random
d={1:'r',2:'p',3:'s'}

c=d[random.randint(1,3)]
p=input("enter 'r' or 'p' or 's'")

if(c==d):
	print("play")

elif(c=='r' and d=='s') or(c=='p' and d=='r') or(c=='s' and d=='p'):
	print("computer begins")
else:
	print("rahul win")