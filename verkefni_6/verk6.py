name = input("Input a name: ")


name_sp = name.split()
name1 = name_sp[0]
name2 = name_sp[1]
name1 = name1.capitalize()
name2 = name2.capitalize()
name2 = name2[:1]
name1 = name1[:-1]
nyja = name2 + '. ' + name1

print(nyja)
