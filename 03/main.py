a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] # Izveido sarakstu

num = int(input("Choose a number: ")) # Jautā lietotājam izvēlēties ciparu

new_list = [] # Izveido jaunu sarakstu

for i in a:
    if i < num: # Pārbauda vai i ir mazāks par skaitli
        new_list.append(i) # Pievieno jaunu sarakstu

print(new_list) # Jaunais saraksts tiek parādīts terminālī