file_name = "output.txt"

user_input = input("Enter text to write to the file: ")
with open(file_name, "w") as file:
    file.write(user_input + "\n")
print(f"Data successfully written to {file_name}.")

extra_input = input("Enter additional text to append: ")
with open(file_name, "a") as file:
    file.write(extra_input + "\n")
print("Data successfully appended.")

print(f"\nFinal content of {file_name}:")
with open(file_name, "r") as file:
    print(file.read())
