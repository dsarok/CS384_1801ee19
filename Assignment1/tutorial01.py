# Function to add two numbers 
def add(num1, num2): 
	addition = num1 + num2
	return addition

# Function to subtract two numbers 
def subtract(num1, num2): 
	subtraction = num1 - num2
	return subtraction

# Function to multiply two numbers 
def multiply(num1, num2): 
	multiplication=num1*num2 
	return multiplication

# Function to divide two numbers 
def divide(num1, num2): 
	division=num1/num2
	return division
		
# Function to add power function
#You cant use the inbuilt python function x ** y . Write your own function
def power(num1, num2):
    num3=1
    for item in range(num2):
    		num3*=num1
    return num3     
	
	
	
# Python 3 program to print GP.  geometric Progression
#You cant use the inbuilt python function. Write your own function
def printGP(a, r, n): 
	gp=[]
	for i in range(0,n):
    		gp.append(a*power(r,i))
	return gp 

# Python 3 program to print AP.  arithmetic Progression
#You cant use the inbuilt python function. Write your own function
def printAP(a, d, n): 
	ap=[]
	for i in range(0,n):
    		ap.append(a+i*d)
	return ap

# Python 3 program to print HP.   Harmonic Progression
#You cant use the inbuilt python function. Write your own function
def printHP(a, d, n): 
	hp=[]
	app=printAP(a,d,n)
	for i in app:
    		hp.append(1/i)
	return hp

print(printAP(2,3,4))
print(printGP(2,3,4))
print(printHP(2,3,4))