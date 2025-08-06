import itertools

def generatePasswordList(name, birthYear, city):
	birthYearShort = birthYear[-2:]
	symbols = ["!", "!!", "?", "??", "#", "##", "+", "++"]

	def lettersToLeet(text):
		leet_map = {
		'a': '4', 'A': '4',
		'e': '3', 'E': '3',
		'i': '1', 'I': '1',
		'o': '0', 'o': '0',
		's': '5', 'S': '5',
		't': '7', 'T': '7',
		}
		return ''.join(leet_map.get(c, c) for c in text)


	parts = [name, city]
	years = [birthYear, birthYearShort]


	base_passwords = []

	for r in [2, 3]:
		for combo in itertools.permutations(parts + years, r):
			year_count = sum(1 for part in combo if part in years)
			if year_count == r: 
				continue
			base_passwords.append(''.join(combo))

	base_passwords = list(set(base_passwords))


	passwords = []

	for base in base_passwords:
		variants = [
			base,
			base[0].lower() + base[1:]
		]


		for variant in variants:
			passwords.append(variant)
			for sym in symbols:
				passwords.append(variant + sym)
				passwords.append(sym + variant)

			leet = lettersToLeet(variant)
			passwords.append(leet)
			for sym in symbols:
				passwords.append(leet + sym)
				passwords.append(sym + leet)

	return sorted(set(passwords))
