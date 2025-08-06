from gui import startGUI

if __name__ == "__main__":
	startGUI()

name = input("Enter target name: ")
birthYear = input("Enter target birth year: ")
city = input("Enter the City the target is living in or was born in: ")

#Output
print("\nGenerated passwords: ")
for pw in passwords: 
	print(pw)



#print(f"Name is: {name} and has on {birthYear} Birthday!")