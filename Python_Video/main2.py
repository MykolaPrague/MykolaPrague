# generatory setri pamet pocitace
'''nums = (3, 5, 10)
squeres = (num * num for num in nums)
print(squeres) #<generator object <genexpr> at 0x000002159315C520>
'''
'''squeres = (num * num for num in range(6))#kulate zavorky 
                                            # ukazuji na generator
print(squeres)
for num in squeres:
    print(num) 
#0
1
4
9
16
25'''
# konvert generator v list
'''nums = (3, 5, 10) 

gen = (num * num for num in nums)
squeres = list(gen)
print(squeres) #[9, 25, 100]'''

# priklad koli setri mista generator oproti listu
'''from sys import getsizeof


squeres_gen = (num * num for num in range(10000))
print(getsizeof(squeres_gen)) # 200

print(type(squeres_gen)) #<class 'generator'>'''

# list
'''squeres_list = [num * num for num in range(10000)]

print(getsizeof(squeres_list)) # 85176

print(type(squeres_list)) # <class 'list'>'''

# class
'''class Car:
    def move(self):
        print("Car is moving")

    def stop(self):
        print("Car stopped")

my_car = Car()
print(my_car) # <__main__.Car object at 0x0000028E91695CD0>
my_car.move()# Car is moving
my_car.stop()# Car stopped'''

'''class Comment:
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0
    
    def upvote(self):
        self.votes_qty += 1

my_coment = Comment("My comment")

print(my_coment)#<__main__.Comment object at 0x0000018361405FA0>
print(type(my_coment))# <class '__main__.Comment'>
print(my_coment.__dict__) #{'text': 'My comment', 'votes_qty': 0}
print(dir(my_coment))# ['__class__', '__delattr__', '__dict__',
                    #'__dir__', '__doc__', '__eq__', '__format__',
                    #  '__ge__', '__getattribute__', '__getstate__', 
                    # '__gt__', '__hash__', '__init__', '__init_subclass__', 
                    # '__le__', '__lt__', '__module__', '__ne__', '__new__', 
                    # '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
                    # '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
                    #  'text', 'upvote', 'votes_qty']'''

'''class Comment:
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0
    
    def upvote(self, qty):# pridame 2 parameter
        self.votes_qty += qty

my_coment = Comment("My comment")

print(my_coment.text)#My comment

print(my_coment.votes_qty)#0

my_coment.upvote(5)
print(my_coment.votes_qty)
'''

# ukol
'''class Image:
    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self, new_resolution):
        self.resolution = new_resolution
        return new_resolution
    def __str__(self):
        return self.title + '.' + self.extension


first_img = Image('1920x1080', 'Dance', 'jpg')

print(first_img.resolution)#1920x1080
print(first_img.title)#Dance
print(first_img.extension)#jpg

first_img.resize('4000x3000')  
print(first_img.resolution)#4000x3000

second_img = Image('8000x5000', "My cat", 'png')
print(first_img)#Dance.jpg
print(second_img)#My cat.png
'''
# @staticmethod
'''class Comment:
    def __init__(self, text):
        self.text = text
    @staticmethod
    def merge_comments(first, second):
        return f"{first} {second}" 
    
my_comment = Comment("My comment")

m_1 =Comment.merge_comments("Thanks", "Excelent.")
print(m_1)# Thanks Excelent.


m_2 = my_comment.merge_comments("Great", "Ok")
print(m_2) # Great Ok'''

# atribut class
'''class Comment:
    total_comments = 0
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0
        Comment.total_comments += 1

first_coment = Comment("First comment")

print(Comment.total_comments) # 1

Comment.total_comments = 10

print(Comment.total_comments) #10 prepiseme  menime
print(first_coment.total_comments)#10 dedi taky vsechny instance
'''
# magicke metody vytvorime vlasni magicky metod
'''class Comment:
    total_comments = 0
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0
    
    def  upvote(self):
        self.votes_qty += 1

    def __add__(self, other):
        return (f"{self.text} {other.text}", self.votes_qty + other.votes_qty)
    
    def rovno(self, other):
        if self.votes_qty == other.votes_qty:
            return True

first_coment = Comment("First comment")
first_coment.upvote()
second_coment = Comment("Second comment")
second_coment.upvote()

print(first_coment + second_coment)

print(first_coment == second_coment)
'''
# vytvorit metof pro porovnani dvuch instance

# dedicnost z inych classov
# vstrojeny class list

'''
class ExtentedList(list):
    def print_list_info(self):
        print(f"List has {len(self)} elements")

custom_list = ExtentedList([3, 5, 2])

custom_list.print_list_info()
'''


# dekoratory
'''def decorator_function(original_fn):
    def wraper_function(*args, **kwargs):
        print("Executed before function")
        result = original_fn(*args, **kwargs)
        print("Executed after function")
        return result
    return wraper_function

@decorator_function
def my_function(a, b):
    print("This is my function")
    return (a, b)

result = (my_function(100, 50))
print(result)
# Executed before function
# This is my function
# Executed after function
# (100, 50)'''


# universalni funkce
'''def log_func_call(fn):
    def wrapper(*args, ** kwargs):
        print(f"Function name: {fn.__name__}")
        print(f"Function arguments are: {args}, {kwargs}")
        result = fn(*args, ** kwargs)
        print(f"Function result: {result}")
        return result
    return wrapper
    
@log_func_call
def mult(a, b):
    return a * b

print(mult(5, 2))
print('')

@log_func_call
def sum(a, b):
    return a + b
print(sum(40.3, 20.7))'''
# Function name: mult
# Function arguments are: (5, 2), {}
# Function result: 10
# 10
# Function name: sum
# Function arguments are: (40.3, 20.7), {}
# Function result: 61.0
# 61.0

# funkce decorator kontrola  na  spatne typy
'''
def validate_args(fn):
    def wrapper(*args, **kwargs):
        for arg in [*args, *kwargs.values()]:
            if not isinstance(arg, int) and not isinstance(arg, float):
                raise ValueError(f"Type of the {arg} is {type(arg)}",
                                 "All arguments must be int or float")
        result = fn(*args, **kwargs)
        return result
    return wrapper
@validate_args
def sum_nums(a, b):
    return a + b
try:
    print(sum_nums(7, 2))
    print(sum_nums(10.5, 2.3))
    print(sum_nums(a=10.5, b='2.0'))
except ValueError as e:
    print(e)
'''
# decorator kontrola na autentefikace user
'''def is_user_autenicated():
    return True


def check_user_auth(func):
    def wrapper(*args, **kwargs):
        if is_user_autenicated():
            print("User id autenticated!")
            return func(*args, **kwargs)
        else:
            raise Exception("User is NOT autenticated!")
    
    return wrapper

@check_user_auth
def do_sensitive_job():
    print("Results of some sensitive tasks")

try:
    do_sensitive_job()
except Exception as e:
    print(e)'''
# module and import

# json


# import json
# convert dict v json and json v dict
'''my_dict = {
    'a': 1,
    'b': (2, 3, 5),
    'c': 'asd',
    'd': None,
    'e': True,
    'f': False
}

converted_dict = json.dumps(my_dict, indent=1)
print(converted_dict)
print(type(converted_dict))

converted_json = json.loads(converted_dict)
print(converted_json)'''

# prace z file # c:\Users\kolja\Desktop\Python\MykolaPrague\Python_Video
''' 
from os import path # funkcionalny spusub vyhledat absolutni cestu
print(path.abspath('.'))

from pathlib import Path # objktno orientovany spusob
print(Path('.').absolute())

from pathlib import Path #cwd -current working directory
print(Path.cwd())

#formirujem cestu 
from pathlib import Path
print(Path('C:/') / 'Users' /'kolja' / 'Desktop'/ 'Python'/ 'MykolaPrague'/ 'Python_Video')'''

# kontrola  existujici slozky
'''from pathlib import Path


print(Path('main.py').exists()) # True
print(Path('main.py').is_file()) # True'''

# seznam slozek

'''for f in Path('.').iterdir():
    print(f)# main.py main2.py'''
# precteme existujici file
'''with open ('test.txt') as test_file:
    print(test_file.read())'''
# precteme existujici file a taky ulozi do listu
'''with open ('test.txt') as test_file:
    print(test_file.readlines())'''  # ['tsdfgdf\n', 'sfsgs']

# stvorime a zapiseme do filu

'''with open('new.txt', 'w') as new_file: 
    new_file.write("First string\n") 
    new_file.write("Second string\n")'''
# precteme file
'''with open('new.txt') as new_file: 
    print(new_file.read())'''
# smazat file
'''from pathlib import Path
my_file = Path('test.txt')

if my_file.exists():
    my_file.unlink()'''
# vytvorit  file a v nem 2 text soubory  zapsat do nej text ,
# precteme  a pak vymazeme oba text soubory a taky file
'''from pathlib import Path

file_dir = Path('files')# stvorime cestu i sam file
file_dir.mkdir(exist_ok=True)# pokud existuje to ne stvorime opet

f_file = file_dir / 'first.txt' # stv promenu i cestu
s_file = file_dir / 'second.txt'# stv promenu i cestu


with open(f_file, 'w') as first_file: # otvirame a zapiseme text
    first_file.write("First string\n")
    first_file.write("First string\n")

with open(f_file) as first_file: # otvirame a cteme
    print(first_file.readline())
    print(first_file.readline())


with open(s_file, 'w') as second_file: # otvirame a zapiseme text
    second_file.write("Second string\n")
    second_file.write("Second string\n")

with open(s_file) as second_file:# otvirame a cteme
    print(second_file.readline())
    print(second_file.readline())


f_file.unlink() # mazeme text soubor

s_file.unlink() # mazeme text soubor


file_dir.rmdir() # mazeme file'''

# CSV
# my_csv.py
'''
import csv
with open('new.txt', 'w') as new_file: 
    new_file.write("First string\n") 
    new_file.write("Second string\n")

with open('c:/Users/kolja/Desktop/Python/GROUP04/PY/16/username.csv') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        print(row)

print('-------------------------------------------------')

with open('c:/Users/kolja/Desktop/Python/GROUP04/PY/16/username.csv') as file:
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        print(row)'''
# time
'''import time

start_time = time.time()

my_range = list(range(100000000))
print(my_range[1000])


end_time = time.time()

print(end_time - start_time)
'''
#random

'''import random

print(random.random())#V
print(random.randint(1, 10))#2
print(random.choice('abcdef'))#e
print(random.choice([1, 10, 5]))#5
print(random.choices([1, 10, 15, 4, 20, 50], k=2))# [50, 10]
my_list = [1, 10, 15, 4, 20, 50]
random.shuffle(my_list)
print(my_list)# [50, 10, 20, 1, 15, 4]


print(''.join(random.choices('ABCDEF0123456789', k=8))) #3CF77331'''

#secret, string generace hesla
'''import secrets
import string

all_chars = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
print(''.join(secrets.choice(all_chars) for i in range(10)))#lQzhH+tDj2
print(string.ascii_letters)#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase)#abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase)#ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)#0123456789
print(string.punctuation)#!"#$%&'()*+,-./:;<=>?@[]^_`{|}~'''

# math
'''
import math
print(math.pi)# 3.141592653589793 
print(math.e)# 2.718281828459045
print(math.sqrt(25))# 5.0 5x5=25
print(math.log(100))# 4.605170185988092
print(math.factorial(10))# 3628800 10*9*8*7*6*5*4*3*2*1'''

# funkce rekurse musi byt ukoncena
'''import math
def calc_factorial(num):
    if type(num) is not int:
        raise TypeError("Number must be ineger")
    if num <= 0:
        raise ValueError("Number must be positive") 
    if num == 1:
        return 1
    return calc_factorial(num - 1) * num

print(calc_factorial(10))
print(math.factorial(10))'''
# regularni vyrazy hledani  porovnani kontrola
'''import re
my_string = "Jour name is Mykola."

res = re.search('M....a', my_string)# . znamena jak koli symvol
res1 = re.search('^J.*n', my_string)#  ^ ukaze na zacatek hledani
res2 = re.search('M....a.$', my_string)# $ ukaze na konec hledani
res3 = re.search('M.*a', my_string)# .* cokoliv
res4 = re.search(r'M....a.$', my_string)# r ne da sped znakam  mod kod


print(res) #<re.Match object; span=(11, 17), match='Mykola'>
           # najde index zacatku a konce stringu

print(res1)
print(res2)
print(res3)
print(res4)
print(res.span())
print(res.start())
print(res.end())


print(type(res))'''
import re
# kontrola emaila

def check_email(email):
    email_regexp = r"^[a-zA-z0-9_.]+@[a-zA-z0-9]+\.[a-zA-z0-9-.]+$"
    email_sheck_pattern = re.compile(email_regexp)
    validation_result = "valid" if email_sheck_pattern.fullmatch(email) else "not valid"
    return (email, validation_result)

print(check_email('bs@gmail.com'))
print(check_email('b.s@sub.gmail.com'))
print(check_email('b.s@gmail.com'))
print(check_email('b_s@gmail.com'))
print(check_email('bsgmail.com'))
print(check_email('bs@gmailcom'))
print(check_email('@gmail.com'))
print(check_email('bs@'))

# kontrola hesla
test_password = 'ASDfas!2342'

def check_password(password):
    length_patern = re.compile(r"\S{8,}")
    lowercase_patern = re.compile(r"[a-z]+") #aspon 1 symvol 
    upercase_patern = re.compile(r"[A-Z]+")
    number_patern = re.compile(r"[0-9]")
    especial_symbol_patern = re.compile(r"[@%#!*^&]")

    if not re.fullmatch(length_patern, password):
        return (False, "Password must have at least 8 symbols")
    
print(check_password(test_password))




# SQL
''' 
import sqlite3

DB_NAME = "sqlite_db.db"



# CREATE NEW TABLE

with sqlite3.connect(DB_NAME) as sqlite_conn:
    print(sqlite_conn)
    print(sqlite3.version)

with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = """CREATE TABLE IF NOT EXISTS courses (
    id iteger PRIMARY KEY,
    title text NOT NULL,
    snudent_gty integer,
    reviews_qty integer
    );"""
    sqlite_conn.execute(sql_request)




#add records to the courses table
courses = [
    (351, "JavaScript course", 415, 100),
    (614, "C++ course", 161, 10),
    (721, "Java full course", 100, 35)
]
with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = "INSERT INTO courses VALUES(?, ?, ?, ?)"
    for course in courses:
        sqlite_conn.execute(sql_request, course)
    sqlite_conn.commit()


with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = "SELECT * FROM courses"
    sql_cursor = sqlite_conn.execute(sql_request)
    # for record in sql_cursor:
    #     print(record[1])
    records = sql_cursor.fetchall()
    print(records)  #[(251, 'Python course', 100, 30),
                    #  (351, 'JavaScript course', 415, 100),
                      #  (614, 'C++ course', 161, 10),
                       #   (721, 'Java full course', 100, 35)]
'''



