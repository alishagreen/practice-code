#snowman 

# Make a word guessing game using functions
snow_1 = "      _     "
snow_2 = "    _|=|_   "
snow_3 = "    ('')    "
snow_4 = ">--( o  )--<"
snow_5 = "  ( o    )  "

snow_man = [snow_1, snow_2, snow_3, snow_4, snow_5]

def print_snow(snow_man):
	for snow in snow_man:
		print snow 

answer = "python"

guess = raw_input("Guess a letter:")

if guess in answer:
	print "You guessed it!"
else: 
	print_snow()

