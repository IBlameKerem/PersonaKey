import tkinter as tk
from tkinter import messagebox, filedialog

from generator import generatePasswordList
from utils import savePasswordsToFile

def startGUI():
	def onGenerate():
		name = entryName.get()
		birthYear = entryBirthYear.get()
		city = entryCity.get()

		if not (name and birthYear and city):
			messagebox.showwarning("Error", "Please fill in everything!")
			return

		passwords = generatePasswordList(name, birthYear, city)

		textOutput.delete("1.0", tk.END)
		for pw in passwords:
			textOutput.insert(tk.END, pw + "\n")

		textOutput.passwords = passwords

	def onSave():
		if not hasattr(textOutput, 'passwords') or not textOutput.passwords:
			messagebox.showwarning("Error", "Empty Data")
			return
		filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Textfile", "*.txt")], title = "Saves as")

		if filepath:
			savePasswordsToFile(textOutput.passwords, filepath)
			messagebox.showinfo("Saved", f"Succesfully saved: \n{filepath}")

	root = tk.Tk()
	root.title("PersonaKey")
	root.geometry("500x500")

	tk.Label(root, text="Name: ").pack()
	entryName = tk.Entry(root)
	entryName.pack()

	tk.Label(root, text="Birth Year:").pack()
	entryBirthYear = tk.Entry(root)
	entryBirthYear.pack()

	tk.Label(root, text="City:").pack()
	entryCity = tk.Entry(root)
	entryCity.pack()

	tk.Button(root, text="Generate passwords", command=onGenerate).pack(pady=10)

	textOutput = tk.Text(root, height=15, width=60)
	textOutput.pack()

	tk.Button(root, text="Save as .txt", command=onSave).pack(pady=10)

	root.mainloop()