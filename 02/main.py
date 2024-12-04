""" Method 1 """ # 1. metode

num = int(input("Give me a number to check: ")) # Jautā lietotājam skaitli, ko pārbaudīt
check = int(input("Give me a number to divide by: ")) # Jautā lietotājam skaitli ar ko dalīt

if num % 4 == 0: # Ja skaitļa dalīšanas atlikums ar 2 ir 0
    print(num, "is a multiple of 4")
elif num % 2 == 0: # Ja skaitļa dalīšanas atlikums ar 2 ir 0
    print(num, "is an even number") # Izvada terminālī, ka ir pāra skaitlis
else:
    print(num, "is an odd number") # Izvada terminālī, ka ir nepāra skaitlis

if num % check == 0:
    print(num, "divides evenly by", check) # Izvada terminālī, ka skaitlis dalās
else:
    print(num, "doesn't divide evenly by", check) # Izvada terminālī, ka skaitlis nedalās


""" Method 2 """ # 2. metode

num = int(input("Enter a number: ")) # Jautā lietotājam ievadīt skaitli
mod = num % 2
if mod > 0:
    print("You picked an odd number.") # Izvada terminālī, ka lietotājs izvēlējās nepāra
else:
    print("You picked an even number.") # Izvada terminālī, ka lietotājs izvēlējās pāra skaitli
