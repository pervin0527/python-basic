import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
voca_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(voca_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a words: ").upper()
result = [voca_dict[x] for x in user_input]
print(result)
