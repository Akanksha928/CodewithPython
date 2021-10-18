import pandas

alphabets = pandas.read_csv("nato_phonetic_alphabet.csv", index_col=0, squeeze=True).to_dict()
name = input("Enter your name: ").upper()
result = [alphabets[n] for n in name]
print(result)




