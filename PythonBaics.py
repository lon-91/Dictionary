with open("veges.txt", "a+") as file:
    content = file.write("Cabbage\n kale's\n ")
    file.seek(0)
    content = file.read()
    print(content)