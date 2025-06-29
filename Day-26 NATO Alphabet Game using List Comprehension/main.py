import random
numbers = [1,2,3]

new_list = [n+1 for n in numbers]


new_range_list = [n * 2 for n in range(1,5)]


names = ["Alex", "Bath", "Caroline", "Dave", "Elanor", "Freddie"]

# short_names = [name for name in names if len(name) < 5]
#
# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [int(n) for n in list_of_strings]
# result = [n for n in numbers if n % 2 == 0]
# print(result)

student_scores = {name:random.randint(1,100) for name in names }

passed_students = {name:score for (name,score) in student_scores.items() if score >= 60}
# print(passed_students)

import pandas

# student_dict = {
#     "student": ["Angela", "James","Lilly"],
#     "score":[56,76,98]
# }

# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# for (index,row) in student_data_frame.iterrows():
#     if row.student == "Angela":
#         print(row)


phonetic_alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter:row.code for (index, row) in phonetic_alphabets.iterrows()}

word = input("Enter a word:").upper()

result = [phonetic_dict[letter] for letter in word]
print(result)
