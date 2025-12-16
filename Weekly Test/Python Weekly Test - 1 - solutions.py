# Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.
text = "Hello World"
text.lower()
'hello world'

greeting = "good morning"
greeting.upper()
'GOOD MORNING'

data = " python "
data.strip()
'python'

line = "Python is tough"
line.replace("tough","easy")
'Python is easy'

word = "banana"
word.count('a')
3

text = "python is fun"
text.split()
['python', 'is', 'fun']
sentence = "learn python"
len(sentence)
12

sentence = "learn python"
sentence.isalnum()
False

text = "HELLO"
res=text.lower()
res.capitilize()
'Hello'

email = "student@domain.com"
email.endswith()
email.endswith(".com")
True

numbers = [45, 67, 89, 32]
numbers.sort()
numbers
[32, 45, 67, 89]
sorted(numbers)
[32, 45, 67, 89]

nums = [10, 20, 30]
nums.append(40)
nums
[10, 20, 30, 40]

colors = ["red", "blue", "green"]
colors.remove("blue")
colors
['red', 'green']

values = [1, 2, 3, 2, 1]
values.count(2)
2

items = ["pen", "book", "pencil"]
','.join(items)
'pen,book,pencil'

scores = [100, 90, 80]
scores[::-1]
[80, 90, 100]

scores.reverse()
scores
[80, 90, 100]

students = ("Anu", "Ravi", "Meena")
students[1]
'Ravi'

details = ("ID101", "Sita", "CSE")
list(details)
['ID101', 'Sita', 'CSE']

data = (5, 3, 9, 1)
max(data)
9

group = ("A", "B", "C", "D")
group[-2::]
('C', 'D')

a = "10"
b = "20"
int(a)+int(b)
30

num=25
str(num)
'25'

x=10
y=3
x%y
1

a=5
b=2
a**b
25

p=15
q=20
p<q
True

numbers = [1, 2, 3, 4, 5]
sum(numbers)
15

data = [3, 7, 1, 9]
max(data)
9

word = "mississippi"
word.count('s')
4

text = "I love Python"
text.replace("love","learn")
'I learn Python'

values = [10, 20, 30, 40]
tuple(values)
(10, 20, 30, 40)
