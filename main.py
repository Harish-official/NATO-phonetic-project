import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

#Create a dictionary in this format:
data_dict = {row.letter:row.code for (index,row) in data.iterrows()}
print(data_dict)

#Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a Name: ")
string_name = [i.upper() for i in user_input]

new_list = [data_dict[n] for n in string_name]
print(new_list)
