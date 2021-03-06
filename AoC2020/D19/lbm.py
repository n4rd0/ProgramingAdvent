def parse_input():
	with open("input19.txt") as f:
		inp = f.read().split('\n\n')
	
	words = inp[1].strip().split('\n')
	rules = []

	for rule in inp[0].split('\n'):
		# e.g.
		# 12: "b"
		# 120: 113 12 | 68 106
		rule, productions = rule.split(': ')
		productions = [prod.split(' ') for prod in productions.split(' | ')]
		productions = [tuple(map(int, prod)) if prod[0][0] != '"' else prod[0][1:-1] for prod in productions]
		
		rules.append([int(rule), productions])

	return words, dict(rules)


def is_word_valid_1(rules, word):
	valid, rest = is_valid(rules, word, 0)
	# Returning an empty word means every character matched
	return not rest


def is_word_valid_2(rules, word):
	repetitions = 0
	valid = True

	while word and valid:
		valid, word = is_valid(rules, word, 42)
		repetitions += 1

	if valid or repetitions <= 2:
		return False 
	
	repetitions -= 1

	valid = True
	while word and valid:
		valid, word = is_valid(rules, word, 31)
		repetitions -= 1
	
	# It is valid when there are more pieces generated by rule 42 than by rule 31
	# 0: 42**(m+n) 31**n,		n, m >= 1
	if repetitions > 0 and not word:
		return True 

	return False
	

def is_valid(rules, word, next_rule):
	if not word:
		return False, []

	if next_rule in ['a', 'b']:
		if word[0] == next_rule:
			return True, word[1:]
		else:
			return False, []

	for prod_seq in rules[next_rule]:
		current_word = word

		for prod in prod_seq:
			is_word_valid, current_word = is_valid(rules, current_word, prod)
			if not is_word_valid:
				break

		if is_word_valid:
			return True, current_word

	return False, word
	

words, rules = parse_input()

print("Star 1:", sum(is_word_valid_1(rules, word) for word in words))
print("Star 2:", sum(is_word_valid_2(rules, word) for word in words))