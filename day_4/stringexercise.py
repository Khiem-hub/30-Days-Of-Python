# 1
first_word = "Thirty"
second_word = "Days"
third_word = "Of"
fourth_word = "Python"
sentence = first_word + " " + second_word + " " + third_word + " " + fourth_word
print(sentence)

# 2
first_word = "Coding"
second_word = "For"
third_word = "All"
sentence = first_word + " " + second_word + " " + third_word
print(sentence)

# 3
company = "Coding For All"

# 4
print(company)

# 5
length_of_company = len(company)
print(length_of_company)

# 6
upper_case_company = company.upper()
print(upper_case_company)

# 7
lower_case_company = company.lower()
print(lower_case_company)

# 8
captalized_company = company.capitalize()
title_case_company = company.title()
swap_case_company = company.swapcase()
print("{} \n{} \n{}".format(captalized_company, title_case_company, swap_case_company))

# 9
cut_out_first_word = company[7:14]
print(cut_out_first_word)

# 10
find_coding = company.find("Coding")
if find_coding != -1:
    print("The word 'Coding' is found at index:", find_coding)
else:
    print("The word 'Coding' is not found.")

# 11
replace_coding = company.replace("Coding", "Python")
print(replace_coding)

# 12
python_for_everyone = "Python for Everyone"
replace_for_everyone = python_for_everyone.replace("Everyone", "All")
print(replace_for_everyone)

# 13
split_company = company.split()
print(split_company)

# 14
split_all = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
split_companies = split_all.split(", ")
print(split_companies)

# 15
first_character = company[0]
print(first_character)

# 16
last_character = company[-1]
print(last_character)

# 17
character_at_index_10 = company[10]
print(character_at_index_10)

# 18
# 1st method
phrase = 'Python For Everyone'
acronym = ''.join(word[0] for word in phrase.split()).upper()
print(acronym)  # PFE
# 2nd method
phrase = 'Python For Everyone'
acronym = phrase[0] + phrase[7] + phrase[11]
print(acronym)  # PFE

# 19 
phrase = "Coding For All"
acronym = phrase[0] + phrase[7] + phrase[11]
print(acronym)  # CFA

# 20
first_c_position = company.index('C')
print(first_c_position)  # 0

# 21
first_f_position = company.index('F')
print(first_f_position)  # 7

# 22
phrase = "Coding For All People"
r_index_find_l = phrase.rindex('l')
print(r_index_find_l)  # 19

# 23 + 26: giong nhau
phrase = "You cannot end a sentence with because because because is a conjunction"
first_because_index = phrase.index("because")
print(first_because_index)  # 31

# 24
phrase = "You cannot end a sentence with because because because is a conjunction"
last_because_index = phrase.rindex("because")
print(last_because_index)  # 47

# 25 + 27: giong nhau
phrase = "You cannot end a sentence with because because because is a conjunction"
sub_phrase = "because because because"
start = phrase.index(sub_phrase)
end = start + len(sub_phrase)
slice_out = phrase[start:end]
print(slice_out)

# 28
print(company.startswith('Coding'))  # True

# 29
print(company.endswith('Coding'))  # False

# 30
remove_trailing_space = company.strip()
print(remove_trailing_space)  # "Coding For All"

# 31
print("30DaysOfPython".isidentifier())  # False, because it starts with a number/digit
print("thirty_days_of_python".isidentifier())  # True

# 32
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libraries = ' # '.join(libraries)
print(joined_libraries)

# 33
sentence = "I am enjoying this challenge.\nI just wonder what is next."
print(sentence)

# 34
tabbed_sentence = "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
expanded_tabbed_sentence = tabbed_sentence.expandtabs(10)
print(expanded_tabbed_sentence)

# 35
radius = 10
pi = 3.14
area = pi * radius ** 2
print("The area of a circle with radius {} is {} meters square.".format(radius, int(area)))

# 36
a = 8 
b = 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))  
print('{} / {} = {}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b)) 
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))  


