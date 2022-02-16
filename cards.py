
import random
from decimal import Decimal

counter_win = Decimal(0)
counter_lost = Decimal(0)

def main():
	global counter_win
	global counter_lost	

	arr_of_cards = [(i % 14, 'mast') for i in range(1, 53)]

	for i in range(len(arr_of_cards)):
		if 0 <= i < 13:
			arr_of_cards[i] = (i % 13 + 1, 'heart')
		elif 26 >= i >= 13: 
			arr_of_cards[i] = (i % 13 + 1, 'clubs')
		elif 39 >= i > 26:
			arr_of_cards[i] = (i % 13 + 1, 'spades')
		else:
			arr_of_cards[i] = (i % 13 + 1, 'diamond')

	random.shuffle(arr_of_cards)

	masti = ['heart', 'clubs', 'spades', 'diamond']

	kozur = random.choice(masti)
	#print(kozur)
	#kozur = 'heart'

	two_cards = random.sample(arr_of_cards, 2)

	first_card = two_cards[0]
	second_card = two_cards[1]

	if first_card[1] == second_card[1]:
		counter_win += 1
	elif first_card[1] == kozur and second_card[1] != kozur:
		counter_win += 1
	elif first_card[1] != kozur and second_card[1] == kozur:
		counter_win += 1
	else:
		counter_lost += 1
	# for i, j in arr_of_cards:
		# print(i, j)

if __name__ == '__main__':
	for i in range(10000):
		main()
	print(f'The stat is {counter_win / (counter_win + counter_lost)}')