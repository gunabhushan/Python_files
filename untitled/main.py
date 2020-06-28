import random

answer = random.randint(1,10)


def guesser(guess,answer):
		if 0 < guess < 11:
			if guess == answer:
				print('you are a genius!')
				return True
		else:
			print('please enter a number 1~10')
			return False


if __name__ == '__main__':

	while True:
		try:
			guess = int(input(f'guess a number 1~10:  '))
			if guesser(guess,answer):
				break
		except ValueError as err:
			print('please enter a number')