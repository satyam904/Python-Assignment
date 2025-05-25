try:
    with open("file.txt", "r") as file:
        content = file.read()
        print("File content:\n", content)
except FileNotFoundError:
    print("Error: 'file.txt' not found. Creating a new file.")
    with open("file.txt", "w") as file:
        file.write("Hello world.\nWelcome to Python.")
    print("'file.txt' has been created.")