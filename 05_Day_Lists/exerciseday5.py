# Day 5 - Lists Exercises

#1 Declare an empty list
lst = list()
print("Empty list:", lst)

#2 Declare a list with more than 5 items
fruits = ['apple', 'banana', 'orange', 'grape', 'mango', 'pineapple']
print("List with more than 5 items:", fruits)

#3 Find the length of your list
print("Length of fruits list:", len(fruits))

#4 Get the first item, the middle item and the last item of the list
first_item = fruits[0]
middle_item = fruits[len(fruits)//2]
last_item = fruits[-1]
print("First item:", first_item)
print("Middle item:", middle_item)
print("Last item:", last_item)

#5 Declare a list called mixed_data_types
mixed_data_types = ['John Doe', 25, 175.5, 'Single', '123 Main Street']
print("Mixed data types:", mixed_data_types)

#6 Declare a list variable named it_companies
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#7 Print the list using print()
print("IT Companies:", it_companies)

#8 Print the number of companies in the list
print("Number of companies:", len(it_companies))

#9 Print the first, middle and last company
print("First company:", it_companies[0])
print("Middle company:", it_companies[len(it_companies)//2])
print("Last company:", it_companies[-1])

#10 Print the list after modifying one of the companies
it_companies[0] = 'Meta'  # Changed Facebook to Meta
print("After modifying first company:", it_companies)

#11 Add an IT company to it_companies
it_companies.append('Tesla')
print("After adding Tesla:", it_companies)

#12 Insert an IT company in the middle of the companies list
middle_index = len(it_companies) // 2
it_companies.insert(middle_index, 'Netflix')
print("After inserting Netflix in middle:", it_companies)

#13 Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()  # Change Meta to uppercase
print("After changing Meta to uppercase:", it_companies)

#14 Join the it_companies with a string '#; '
companies_string = '#; '.join(it_companies)
print("Joined companies:", companies_string)

#15 Check if a certain company exists in the it_companies list
print("Is Google in the list?", 'Google' in it_companies)
print("Is Twitter in the list?", 'Twitter' in it_companies)

#16 Sort the list using sort() method
it_companies_copy = it_companies.copy()  # Make a copy to preserve original
it_companies_copy.sort()
print("Sorted companies:", it_companies_copy)

#17 Reverse the list in descending order using reverse() method
it_companies_copy.reverse()
print("Reversed companies:", it_companies_copy)

#18 Slice out the first 3 companies from the list
first_three = it_companies[:3]
print("First 3 companies:", first_three)

#19 Slice out the last 3 companies from the list
last_three = it_companies[-3:]
print("Last 3 companies:", last_three)

#20 Slice out the middle IT company or companies from the list
middle_start = len(it_companies) // 2 - 1
middle_end = len(it_companies) // 2 + 2
middle_companies = it_companies[middle_start:middle_end]
print("Middle companies:", middle_companies)

#21 Remove the first IT company from the list
it_companies_temp = it_companies.copy()
it_companies_temp.pop(0)
print("After removing first company:", it_companies_temp)

#22 Remove the middle IT company or companies from the list
it_companies_temp = it_companies.copy()
middle_index = len(it_companies_temp) // 2
it_companies_temp.pop(middle_index)
print("After removing middle company:", it_companies_temp)

#23 Remove the last IT company from the list
it_companies_temp = it_companies.copy()
it_companies_temp.pop()
print("After removing last company:", it_companies_temp)

#24 Remove all IT companies from the list
it_companies_temp = it_companies.copy()
it_companies_temp.clear()
print("After removing all companies:", it_companies_temp)

#25 Destroy the IT companies list
del it_companies_temp
print("IT companies list destroyed")

#26 Join the following lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack_web = front_end + back_end
print("Joined lists:", full_stack_web)

#27 Copy the joined list and insert Python and SQL after Redux
full_stack = full_stack_web.copy()
redux_index = full_stack.index('Redux')
full_stack.insert(redux_index + 1, 'Python')
full_stack.insert(redux_index + 2, 'SQL')
print("Full stack after adding Python and SQL:", full_stack)
