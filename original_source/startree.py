# get height from user
height = eval(input("Enter height of tree: "))

#draw each row
row = 0
while row < height:
	#print spaces if needed (if not last row)
	count = 0
	while count < height - row:
		print(' ', end = "")
		count += 1


	#print stars
	count = 0
	while count < 2*row + 1:
		print ("*", end = "")
		count += 1

	#start a new line for next row
	print()
	row += 1 #increment