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
		

def power(num1, num2):
    num3=1
    for item in range(num2):
    		num3*=num1
    return num3     
	
def printGP(a, r, n): 
	gp=[]
	for i in range(0,n):
    		gp.append(a*power(r,i))
	return gp 

def printAP(a, d, n): 
	ap=[]
	for i in range(0,n):
    		ap.append(a+i*d)
	return ap
def printHP(a, d, n): 
	hp=[]
	app=printAP(a,d,n)
	for i in app:
    		hp.append(1/i)
	return hp
