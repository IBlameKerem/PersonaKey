def savePasswordsToFile(passwords, filepath):
	with open("persona-keys.txt", "w", encoding="utf-8") as file:
		for pw in passwords:
			file.write(pw + '\n')