import random

the_number = random.randint (0, 100)



def main():
	guess = -1
	print_header ()
	name = input ("Player, what is your name? ")
	print ()

	while guess != the_number:
		guess = int (input ("Enter a number between 0 and 100: "))
		if guess < the_number:
			print ("Sorry {}, your guess of {} is to Low.".format (name, guess))

		elif guess > the_number:
			print ("Sorry {}, your guess of {} is to High.".format (name, guess))

		else:
			print ("Excellent work {}, you won, the number is {}".format (name, the_number))


def print_header():
	print ("--------------------------------------------------------------------------")
	print ("                         Guess the number")
	print ("--------------------------------------------------------------------------")
	print ()


if __name__ == '__main__':
	main ()
