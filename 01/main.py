""" Insert Name """ # Ievada vārdu
name = input("Whats your name: ") # Jautā lietotāja vārdu

""" Insert age. Also convert age into an Integer value """ # Ievada vecumu
age = int(input("How old are you: ")) # Jautā lietotāja vecumu - cik ir gadi

""" Do the math """ # Izrēķina rezultātu
year = str((2018 - age)+100) # Aprēķina kurā gadā lietotājam būs 100 gadi

""" Print the result """ # Parāda rezultātu
print(name + " will be 100 years old in the year " + year) # Rezultāts parādās terminālī
