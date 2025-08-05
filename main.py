name = input("Enter target name: ")
birthYear = input("Enter target birth year: ")


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




base_passwords = [
	name + birthYearShort,
	name + birthYear,
	birthYearShort + name,
	birthYear + name
]



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

passwords = list(set(passwords))


#Output
print("\nGenerated passwords: ")
for pw in passwords: 
	print(pw)


#print(f"Name is: {name} and has on {birthYear} Birthday!")