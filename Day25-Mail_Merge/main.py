#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("./Input/Names/invited_names.txt") as f:
    names = f.readlines()
f.close()
  
with open("./Input/Letters/starting_letter.txt", "r") as f:
    letter_content = f.read()

    for name in names:
        name = name.strip()
        new_letter = letter_content.replace("[name]", name)
        with open(f"./Output/ReadyToSend/{name}_letter.txt", "w") as letter:
            letter.write(new_letter)
        letter.close()
f.close()