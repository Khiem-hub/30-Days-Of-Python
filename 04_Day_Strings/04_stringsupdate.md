<div align="center">
  <h1> 30 Days Of Python: Day 4 - Strings</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>


Author:
Asabeneh Yetayeh
Modernized for Python 3.8+


</div>


<< Day 3￼ | Day 5 >>￼

	•	Day 4￼
	•	Strings￼
	•	Creating a String￼
	•	String Concatenation￼
	•	Escape Sequences in Strings￼
	•	String formatting￼
	•	String Interpolation / f-Strings (Python 3.6+)￼
	•	Python Strings as Sequences of Characters￼
	•	Accessing Characters in Strings by Index￼
	•	Slicing Python Strings￼
	•	Reversing a String￼
	•	Skipping Characters While Slicing￼
	•	String Methods￼
	•	💻 Exercises - Day 4￼

<h1> Day 4

## Strings

Text is a string data type. Any data written as text is a string. Any data under single, double or triple quotes are strings. There are different string methods and built-in functions to deal with string data types. To check the length of a string use the len() function.

### Creating a String
```sh
letter = 'P'
print(letter)               # P
print(len(letter))          # 1

greeting = 'Hello, World!'
print(greeting)             # Hello, World!
print(len(greeting))        # 13

sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence)
```
### Multiline string is created by using triple single (''') or triple double quotes (""").
```sh
multiline_string = '''I am learning Python.
It is simple and powerful.'''
print(multiline_string)

multiline_string = """This is another way
to write multiline strings."""
print(multiline_string)
```
### String Concatenation

We can connect strings together. Merging or connecting strings is called concatenation.
```sh
first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = first_name + space + last_name
print(full_name) # Asabeneh Yetayeh

print(len(first_name))
print(len(last_name))
print(len(full_name))
```
### Escape Sequences in Strings

In Python, \ followed by a character is an escape sequence.
	•	\n: new line
	•	\t: tab character
	•	\\: backslash
	•	\': single quote
	•	\": double quote
```sh
print('I hope everyone is enjoying the Python Challenge.\nAre you ?')
print('Days\tTopics\tExercises')
print('Day 1\t5\t5')
print('This is a backslash (\\)')
print('It starts with "Hello, World!"')
```
### String formatting

String Interpolation / f-Strings (Python 3.6+)
Strings start with f and allow variable injection directly.
```sh
a = 4
b = 3
print(f'{a} + {b} = {a + b}')
print(f'{a} / {b} = {a / b:.2f}')
```
⚠️ Old % formatting and str.format() are intentionally removed to focus on modern Python.

Python Strings as Sequences of Characters

Python strings are sequences of characters.

### Accessing Characters in Strings by Index
```sh
language = 'Python'
print(language[0])   # P
print(language[1])   # y
print(language[-1])  # n
```
### Slicing Python Strings
```sh
language = 'Python'
print(language[0:3])
print(language[3:])
print(language[-3:])
```
### Reversing a String
```sh
greeting = 'Hello, World!'
print(greeting[::-1])
```
### Skipping Characters While Slicing
```sh
language = 'Python'
print(language[0:6:2])
```
### String Methods

Some commonly used string methods:
```sh
text = 'Coding For All'
print(text.upper())
print(text.lower())
print(text.title())
print(text.find('Coding'))
print(text.replace('Coding', 'Python'))
print(text.split(' '))
print(' '.join(['HTML', 'CSS', 'JavaScript']))
print(text.strip())
print('thirty_days_of_python'.isidentifier())
```

## 💻 Exercises - Day 4

### Example output format (shell)

The area of a circle with radius 10 is 314
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144

	1.	Concatenate ‘Thirty’, ‘Days’, ‘Of’, ‘Python’ into one string.
	2.	Declare a variable company = "Coding For All".
	3.	Print the length of the company string.
	4.	Change all characters to uppercase.
	5.	Change all characters to lowercase.
	6.	Slice out the first word of Coding For All.
	7.	Replace Coding with Python.
	8.	Split the string using space.
	9.	Join ['Django', 'Flask', 'FastAPI'] using # .
	10.	Use f-string to display the area of a circle.

🎉 CONGRATULATIONS! 🎉

<< Day 3￼ | Day 5 >>￼