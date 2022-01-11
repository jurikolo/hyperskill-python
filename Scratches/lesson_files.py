# task 1
# my_file = open("file.txt", "r")
# for line in my_file:
#     print(line)
#     if line in ["summer\n", "summer"]:
#         print("a")

# task 2
# my_file = open("file.txt", "r")
# for line in my_file:
#     a, b = line.split(" ")
#     print(int(a) + int(b))
# my_file.close()

# task 3
# my_file = open("file_w.txt", "w")
# text = "row1\nrow2\nrow3\n"
# my_file.write(text)
# my_file.close()

# task 4
# old_file = open("animals.txt", "r")
# animals = old_file.read()
# old_file.close()
# animals = animals.replace("\n", " ")
# new_file = open("animals_new.txt", "w")
# new_file.write(animals)
# new_file.close()

# task 5, open multiple files and work with these using tuple
with open('name.txt') as f1, open('surname.txt') as f2, open('full_name.txt', 'w') as f3:
    name = f1.read()
    surname = f2.read()

    full_name = name + ' ' + surname

    f3.write(full_name)
