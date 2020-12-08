
def oddEven(numberList):
	even,odd = [], []

	for i in numberList:
		even.append(i) if i%2 == 0 else odd.append(i)
	
	return even,odd

def firstStar(numberList):
	even,odd = oddEven(numberList)
	good_ending = False

	while not good_ending and len(numberList) > 0 :
		number_1 = numberList.pop()
		for number_2 in (even if number_1%2 == 0 else odd):
			if number_1 + number_2 == 2020:
				good_ending = True
				result = number_1 * number_2

	return result if good_ending else -1


def secondStar(numberList):
	even, odd = oddEven(numberList)
	good_ending = False

	while not good_ending and len(numberList) > 0:
		number_1 = numberList.pop()
		for number_2 in even:
			sum_12 = number_1 + number_2
			if sum_12 < 2020:
				for number_3 in (even if sum_12%2 == 0 else odd):
					if sum_12 + number_3 == 2020:
						good_ending = True
						result = number_1 * number_2 * number_3

	return  result if good_ending else -1


with open('input.txt') as file:
	input_list = [int(i) for i in file.readlines()]		

print(firstStar(list(input_list)))
print(secondStar(list(input_list)))