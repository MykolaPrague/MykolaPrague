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

#ukol 
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
#Function name: mult
# Function arguments are: (5, 2), {}
# Function result: 10
# 10
# Function name: sum
# Function arguments are: (40.3, 20.7), {}
# Function result: 61.0
# 61.0

#funkce decorator kontrola  na  spatne typy 
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
def is_user_autenicated():
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
    print(e)
