#mult-tables 

table = int(raw_input("Enter a number to see its multiplication table:")) 

for i in range(1,11): 
	prod = table*i 
	print str(table) + " x " + str(i) + " = " + str(prod) 


