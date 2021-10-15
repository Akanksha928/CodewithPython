PLACEHOLDER = "[name]"

with open(r"Input/Names/invited_names.txt") as file:
    names = file.readlines()
print(names)

with open(r"Input/Letters/starting_letter.txt") as file:
    contents = file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = contents.replace(PLACEHOLDER, stripped_name)
        with open(f"Output//ReadyToSend//letter_to_{stripped_name}.docx", mode="w") as file:
            file.write(new_letter)
