import hashlib

def savePasswordsToFile(passwords, filepath, hashOptions):
	def ntlm_hash(text):
		return hashlib.new('md4', text.encode('utf-16le')).hexdigest()

	with open(filepath, "w", encoding="utf-8") as file:
		for pw in passwords:
			lines = []

			if not any(hashOptions.values()):
				lines.append(pw)

			if hashOptions.get("md5"):
				lines.append(hashlib.md5(pw.encode()).hexdigest())

			if hashOptions.get("sha1"):
				lines.append(hashlib.sha1(pw.encode()).hexdigest())

			if hashOptions.get("ntlm"):
				lines.append(ntlm_hash(pw))

			for line in lines:
				file.write(line + "\n")