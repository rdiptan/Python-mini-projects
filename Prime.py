
def prime(num):
	for i in range(2, num):
		if(num%i == 0):
			return True
		else:
			return False
		print("Prime")
		
num = int(input("Enter a number."))
ans = prime(num)
if ans:
	print("Not prime")
else:
	print("prime")
		



