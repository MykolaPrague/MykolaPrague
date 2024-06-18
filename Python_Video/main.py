
'''def sum_nums(a, b):
    sum = a + b
    print("Line is not defind")
    return sum


first_sum = sum_nums(10, 5)
print(first_sum)'''


'''print(print(print(5+5)))
print('Hello', input("Enter your name: "),'!')
def user_name(first_name, second_name):
    user_name = first_name + ' ' + second_name


    return user_name

full_name = user_name('Mykola', 'Shyshka')
print(full_name)'''

'''snake_case = (variabilní,funkce, metody,moduly)
PascalCase(class)
my-package(knihovny)
DB_PASSWORD(const)'''

# datove typy
'''my_int = 10 
my_float = 85.5
my_string = 'abc'
my_boolean = True
my_nic = None
my_list = []'''


'''a = 'abc'
a = 10
a = True
a = None'''


'''def print_name(name):
    print(name)

print_name('Mykola')  '''

'''print_name = 15 '''  # menime promenu z stringu na int bude chyba
'''print_name('Mykola')'''  # chyba

# jak spravne jmenovat
'''promenna (podstatné jméno(ukaze na to co  v tom je))
funkce a metod (sloveso ukaze to co bude delat ,menit, vracet)'''


# typy a struktura
'''immutable'''
# nelze zmenit typ objektu  (string, boolean, int, float, tuple, None)
'''mutable'''
# lze menit typ objektu (list, dict, set, user-defind class)

# premenne
'''my_name'''  # ->odkaz na object ('sam_objekt')
'''my_name = name'''  # pri zmene nazvu(odkazu) vytvorime novy object ne menime stary a stary se smaze


# odkaz na object
'''my_number = 10 
print(id(my_number))

my_string = 'abc'
print(id(my_string))'''
# nekolik promen muze se odkazovat na  1 object

'''my_number = 10 
print(id(my_number))
#140718985976536


other_number = my_number
print(id(other_number))
#140718985976536'''

# pri kazdem spusteni bude nove id (string)
'''my_name = 'Mykola'
print(id(my_name))'''


# pri kazdem spusteni bude stejne id (int)
'''my_num = 100

print(id(my_num))

other_name = my_num

print(id(other_name))'''

# STRING
'''long_str = """this is a very 
long string"""
print(long_str)

print(type(long_str))
print(id(long_str))'''

# metod pro class str
'''my_comment = "this is my short comment"
print(len(my_comment))
print(my_comment.replace('short', 'long'))  #vytvori novy radek nemeni stary
print(my_comment)
print(my_comment.capitalize())'''

# cele cisla int

'''my_num = int(input("Enter your number: "))# prevod stringu do integeru 
print(pow(my_num, 3)) #zadane cislo do 5^3'''

# float

'''time = 17.25
my_time = int(time)
print(my_time)

str_time = '20.10'
my_time1 = float(str_time)
print(my_time1)'''

# complexna cisla
'''complex_a = 10 + 7j
complex_b = 3 + 3j

print(complex_a + complex_b)'''
# convertace v bool
'''print(bool(10)) -> True
print(bool([])) -> False'''

# porovnani
'''print(100>10) -> True
print('Long'>'long')-> False
print([] == [])->True'''

# convert
'''int_num = 5
float_num = 4.5
print(float_num + int_num)__add__
bool_val = True
int_val = 7
print(int_val + bool_val)__radd__'''
# magic metod
'''print(dir(bool))
print(bool.__doc__)'''
# list
'''my_list = [1, 'pop', True, 25, 'Mykola']
print(my_list)

my_list.pop(2)

print(my_list)
print(len(my_list))

my_list.reverse()
print(my_list)
my_newlist = [800, 10000]
print(my_newlist)

my_list.extend(my_newlist)
print(my_list)'''
# list magic function
'''list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
list3 = list1 + list2
print(list1.__add__(list2))'''

# dictionary
'''my_motorbike = {
    'brand': 'Honda',
    'price': '10000',
}
print(my_motorbike)
my_motorbike['price'] = 7000   #new hodnota
print(my_motorbike['price'])
my_motorbike['is_new'] = True  #add new element
print(my_motorbike)
del my_motorbike['is_new']     #remove element
print(my_motorbike)

key_name ='brand'
my_motorbike[key_name] = 'BMW' #menime HODNOTU klice 
                            #Honda na BMW klic STEJNE 

my_motorbike = {
    'brand': 'Honda',
    'price': '10000',
    'engine_vol': {
        'tort': 25000,
        'is_value': True
    }
}

print(my_motorbike['engine_vol']['tort'])
                        #mnohouroven dictionary'''

'''brand = 'Honda'
price = 10000
engine_vol = 1.2

new_dictionary  = { #creat a new dictionary whith varible
    'brand': brand,
    'price': price,
    'engine_vol': engine_vol,
}
print(new_dictionary)
print(len(new_dictionary))
print(new_dictionary.get('brand'))
print(new_dictionary.get('price', 0))
print(new_dictionary.get('model', 0)) #vyvolame neexistujci klic
dict ={}#creat a new dictionary
print(dict.__doc__)'''

# ukol dictionary
'''my_dict = {}

new_key1 = input("enter your element1: ")
new_hodnota1 = input("enter your hodnota k element1: ")

my_dict[new_key1] = new_hodnota1


new_key2 = input("enter your element2: ")
new_hodnota2 = input("enter your hodnota k element2: ")

my_dict[new_key2] = new_hodnota2

new_key3 = input("enter your element3: ")
new_hodnota3 = input("enter your hodnota k element3: ")

my_dict[new_key3] = new_hodnota3

print(my_dict)'''

# set
'''my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_set = set(my_list)#convert list v set
print(my_set)
my_set.add(10)
print(my_set)
other_set = {1, 3, 5, 7, 9, 11, 13, 15}
print(other_set)
new_set = my_set.intersection(other_set)
new_list2 = list(new_set)
print(new_list2)'''

# range serazene immutable elementy(diapazon)
'''my_range = range(7)#vrati range od 0 do 7 bez 7 
print(my_range)
#range(0, 7)
print(list(my_range))
#[0, 1, 2, 3, 4, 5, 6]
my_range1 = range(10, 20, 3)#10 (prvnni od) , 20 (posledni do) , 3 (krok kazde 3 cilo od 10 do 20 )
print(my_range1)
#range(10, 20, 3)
print(list(my_range1))
#[10, 13, 16, 19]
print(my_range1[0])#10
print(my_range1[1])#13
print(my_range1[2])#16
print(my_range1[3])#19
#print(my_range1[4])#IndexEror'''


# range cykly

'''my_range1 = range(10, 20, 3)
for n in my_range1:
    print(n)


for n in range(10, 20, 3):
    print(n)'''

# range convert
'''my_range = range(10, 20, 3)
print(list(range(10, 20, 3)))
print(tuple(range(10, 20, 3)))
print(set(range(10, 20, 3)))
#print(dict(range(10, 20, 3)))Error'''

# range metod
'''my_range = range(10, 30, 3)
print(my_range.start)
print(my_range.stop)
print(my_range.step)
print(my_range.index(13))# [1]
print(my_range.count(10))# [1]
print(my_range.count(11))# [1]'''

# range ukol
'''my_range = range(5, 20, 5)
mylist = []
for n in my_range:
    mylist.append(n)
print(mylist)'''

# porovnani


'''
# list    mutable      serazene(index)      stejne elementy -> [1, 2]

# tuple   immutable    serazene(index)      stejne elementy -> ()

# set     mutable      neserazene(bez i)    unikatni        -> {}

# range   immutable    serazene(index)      unikatni        -> range()

# dict    mutable      neserazene(bez i)    unikatni        -> {a: 1}

# str     immutable    serazene(index)      stejne elementy -> 1, a '''

# zip funkce

# 2 listy v jeden list tuplu
'''
fruits = ['apple', 'banana', 'lime']
quantities = [100, 70, 50]
dostupnost = ('ano', 'ne', 'ano')

fruits_zip = zip(fruits, quantities, dostupnost) 

fruits_zip_dict = zip(fruits, quantities) 



fruits_list = list(fruits_zip) 


# 2 listy v jeden dict

fruits_dict = dict(fruits_zip_dict) 


print(fruits_list)
#[('apple', 100), ('banana', 70), ('lime', 50)] list tuplu

print(fruits_dict)
#{'apple': 100, 'banana': 70, 'lime': 50} list v dict'''

# kopije hloubkova : kopiruje nezmenne objekty  ktery
# maji v sobe zmenne objekty

'''from copy import deepcopy

info = {
    'name': 'Mykola',
    'is_student': True,
    'points': [],
}
info_deepcopy = deepcopy(info)


info_deepcopy['points'].append(5)

print(info)
#{'name': 'Mykola', 'is_student': True, 'points': []}

print(info_deepcopy)
{'name': 'Mykola', 'is_student': True, 'points': [5]}'''

# Funkce

'''a = 5
b = 3

c = a + b
print(c) #8

a = 8 
b = 12

c = a + b

print(c) #20'''

# funkce
'''def sum(a, b):
    c = a + b
    print(c)

a = 5
b = 3

sum(a,b)

a = 8
b = 12

sum(a,b)'''
# funkce vrati None pokud nepropiseme return
# funkce musima zavolat

'''def my_fn(a,b): # (a, b) -> parametry (muze bit prazdne)
    a = a + 1
    c = a + b
    return c
res = my_fn(10, 3) # parametry (a->10) (b->3) (10,.)-> argumenty
print(res) # 14'''

# funkce z immutable objekty promenami ktere  jsou mimo funkce
'''def my_fn(a,b):
    a = a + 1 # vytvarime novy objekt uvnitr funkce 
    c = a + b
    return c

num_one = 10 # nemenise
num_two = 5
res = my_fn(num_one, num_two)
print(res) # 15
print(num_one) # 10 '''

# funkce z mmutable objekty promenami ktere  jsou mimo funkce

'''def increase_person_age(person):
    person['age'] += 1
    return person

person_one = {            # person a person_one odkazuji na 1 objekt
    'name': 'Bob',        # menime vnejsi objekt uvnitr funkce
    'age': 21
}


increase_person_age(person_one)
print(person_one['age']) # 22'''

# funkce ukol funkce metodem zip objedna 2 listy a pak
# vytvori  novy slovnik dict a pak vrati return

'''def merge_list_to_dict(list_one,list_two):
    list_zip = zip(list_one,list_two)
    return dict(list_zip)
    # nebo v 1 radku:
    return dict(list_zip(list_one,list_two))


a = ['name', 'second_name', 'age']
b = ['I_am', 'two', 50]

my_new_dict = merge_list_to_dict(a, b)
print(my_new_dict)'''

# spojime argumenty  funkce v tuple
'''def sum_nums(*args): jedna * sbere vsechny 
    print(args) #(2, 3, 7)
    print(type(args)) #<class 'tuple'>
    print(args[0]) #2
    return sum(args)
print(sum_nums(2, 3, 7)) #12'''

'''def get_posts_info(name, posts_qty):#sebere jako type
    info = f"{name} wrote {posts_qty} posts"
    return info
info = get_posts_info(name='Mykola', posts_qty=30) # nezalezi na poradi
print(info)'''


'''def get_posts_info(**person): #sebere jako slovnik , dict
    info = f"{person['name']} wrote {person['posts_qty']} posts"
    return info
info = get_posts_info(name='Mykola', posts_qty=30) # nezalezi na poradi
print(info)'''


# argumenty ukol

'''def merge_list_to_dict(list_one,list_two):
    # list_zip = zip(list_one,list_two)
    # return dict(list_zip)
    # nebo v 1 radku:
    return dict(zip(list_one,list_two))


a = ['name', 'second_name', 'age']
b = ['I_am', 'two', 50]
# nebo 
# my_new_dict = merge_list_to_dict(a, b)

my_new_dict = merge_list_to_dict(list_one= ['name', 'second_name', 'age'], list_two=['I_am', 'two', 50])
print(my_new_dict)

my_new_dict1 = merge_list_to_dict(list_two=['I_am', 50], list_one= ['name', 'age'], )
print(my_new_dict1) # nezalezi na poradi pokud mame klice

my_new_dict2 = merge_list_to_dict(['I_am', 50], list_two= ['name', 'age'], )
print(my_new_dict2)


# SyntaxError: positional argument follows keyword argument nelze klicovy element poziciovat jak prvni
# my_new_dict3 = merge_list_to_dict(list_two= ['name', 'age'], ['I_am', 50])
# print(my_new_dict3)'''

# ukol argument dict
# 1 varianta #objednat pomoci dict a zip
'''def update_car_info(a, b):  
    car = dict(zip(a, b))
    car['is_available'] = True
    return car

my_car = update_car_info(a=['brand','color', 'price'], b=['BMW','red', 10000])
print(my_car)'''

# 2 varianta objednat pomoci
'''def update_car_info(**car): #ocekava argumenty z klicovymy slovy
    car['is_available'] = True
    return car

print(update_car_info(brand='BMW', price= 10000, color='red'))'''

'''## TypeError: update_car_info() takes 0 positional arguments but 2 were given

#print(update_car_info('BMW', 10000,)) '''
# parametry funkce z vychozim argumentom
'''def mult_by_factor(value, multiplier=1):
    return value * multiplier
print(mult_by_factor(10, 2)) # 20
print(mult_by_factor(5)) # 5'''
# parametry funkce z dynamickym  argumentom

'''
from datetime import date


def get_weekday():
    return date.today().strftime('%A')


def create_new_post(post, weekday=get_weekday()):
    post_copy = post.copy()
    post_copy['created_on_weekday'] = weekday
    return post_copy


initial_post = {
    'id': 243,
    'autor': 'Mykola',
}

post_with_weekday = create_new_post(initial_post)

print(post_with_weekday)'''

# callback funkce

'''def other_fn():
    pass

def fn_with_callback(callback_fn):
    call_back_fn()


fn_with_callback(other_fn)'''


'''def print_number_info(num):
    if (num % 2) == 0:
        print("Entered number is even")
    else:
        print("Entered number is odd")


def process_number(num, callback_fn):
    callback_fn(num)


entered_num = int(input('Entered any number: '))

process_number(entered_num, print_number_info)'''


# def print_number_info(num):
#     if (num % 2) == 0:
#         print("num is even")
#     else:
#         print("num is odd")
#     return num


# print_number_info()


# global ve funkce dokaze prepsat globalni promenu

'''a = 10 
def my_fn():
    global a
    a = 15

my_fn()

print(a) #15'''
# operatory

'''my_list1 = []
my_list2 = [1, 2]'''

# or
'''print(not my_list1)# True
print(not my_list2)# False
print(not not my_list2)# True'''

'''other_list= ['a', 'b']

print(my_list2 or other_list) # [1, 2] vrati prvni pravdive i ne kontroluje dalsi
print(len(my_list2) > 0 or other_list) # True'''

# and

'''my_list1 = [1, 2]
my_dict = {}
my_dict1 = {'a': 20, 'b': 10}
print(my_list1 and my_dict) #{}
print(bool(my_list1 and my_dict1)) # True'''


# operator **
# ** vytvori novy dict
'''button ={
    'width': 200,
    'text': 'Buy',
}
red_button = { # pomoci** vytvori novy dict a prida new klic/hodnota
    **button,
    'color': 'red'
}
print(button) # {'width': 200, 'text': 'Buy'}
print(red_button)# {'width': 200, 'text': 'Buy', 'color': 'red'}'''

#  ** spoji 2 dict

'''button_info = { 
    'text': 'Buy'
    }
button_style = { #  ** spoji 2 dict v jeden
    'color': 'yellow',
    'width': 200,
    'height': 300,
}
button_num = {
    'num1': 1,
    'num2': 2,
}
                    # | spoji slovniky
my_but = button_info | button_style | button_num 

button = {
    **button_info,
    **button_style,
}
print(button) # {'text': 'Buy', 'color': 'yellow',
                # 'width': 200, 'height': 300}
print(my_but) # {'text': 'Buy', 'color': 'yellow',
              #'width': 200, 'height': 300, 'num1': 1, 'num2': 2}'''

# funkce lambda
#

# def mult(a, b):
#     return a * b

'''mult = lambda a, b: a * b
print(mult(10, 5))'''

'''def greeting(greet):
    return lambda name: f"{greet}, {name}!"

morning_greeting = greeting("Good Morning")
print(morning_greeting('Bogdan'))#Good Morning, Bogdan!

evening_greeting = greeting("Good Evening")
print(evening_greeting('Bogdan'))# Good Evening, Bogdan!'''

# ERROR try
'''try:
    print(10/0)
except ZeroDivisionError as e : #division by zero

    print(e)
except TypeError as e : #unsupported operand type(s) 
                        #for /: 'str' and 'int'
    print(e)
else: # vykona se pokud zadne erory ne vznikly
    print("There C") 
    #There division by zero
finally:# vykona se vzdy 
    print('Continue...')# Continue...'''

'''try:
    print(10/0) 
except Exception as e:'''  # Exception libovolna chyba
# dase uchovat chybu do promene e
'''    print(e)'''  # division by zero

# zzzzzzzgenerace chyb

# ukol


'''def image_info(dict):
    
    my_dict = dict
    
    my_dict = {
        'image_id': 5136,
        'image_title': 'my cat',
    }
    print(f"Image '{my_dict['image_title']}' has id {my_dict['image_id']}")

    
image_info(dict)'''

'''def image_info(dict):
    if('image_id' not in dict) or ('image_title' not in dict):
        raise TypeError("Keys image_title and image_id must be present")
    return f"Image '{dict['image_title']}' has id {dict['image_id']}"

print(image_info({'image_id': 5136, 'image_title': 'my cat'}))
try:
    print(image_info({'image_title': 'my cat'}))
except TypeError as e:
    print(e)'''
# upading rozbaleni

'''my_fruits = ['apple', 'banana', 'lime']
my_fruits = ('apple', 'banana', 'lime')

my_apple, my_banana, my_lime = my_fruits #poradi bude jak v listu

print(my_apple) #apple
print(my_banana)#banana
print(my_lime)#lime


my_fruits = ['apple', 'banana', 'lime']

my_apple, *remaining_fruits = my_fruits

print(my_apple) # apple vrati jednu promenu 
print(remaining_fruits) # ['banana', 'lime'] vrati list zbytek
'''
# rozbaleni dict uvnitr ve funkce
'''user_profile = {
    'name': 'Bogdan',
    'comments_qty': 23,
}
 
def user_info(name, comments_qty=0):
    if not comments_qty:
        return f"{name} has no comments"
    return f"{name} has {comments_qty} comments"

print(user_info(**user_profile)) # pri zavolani funkce rozbalime dict``

user_data = ['Bogdan', 23]'''

# rozbaleni list uvnitr ve funkce
'''
def user_info(name, comments_qty=0):
    if not comments_qty:
        return f"{name} has no comments"
    return f"{name} has {comments_qty} comments"

print(user_info(*user_data)) # pri zavolani funkce rozbalime list``
'''
# podminky if, else, elif.

'''my_number =25
if my_number > 0:
    print(my_number, "if positive number")'''

'''person_info ={
    'age': 20
}

if not person_info.get('name'):
    print("name chybi")'''

# kontrola na int
'''num1 = 10
num2 = 5.3
if (num1 > 0 and
    num2 > 0 and
     isinstance(num1, int)and
      isinstance(num2, int) ):
    print("Both numbers are integer and positive")'''
# if , else
'''my_number  = 21.5
if type(my_number) is int:
    print(my_number, "is integer")
else:
    print(my_number, "is not integer")'''

# if , else

'''my_phone = {
    'price': 200,
    #'brand': 'lenovo'
}
if my_phone.get('brand'):#jesli existuje klic brand get (omezi chybu )
    print("Phone's brand is", my_phone['brand'])
else:# jinak se vykona tento blok
    print("There is not phone brand")'''

# if ve funkci z return
'''def nums_info(a, b):
    if(type(a) is not int) or (type(b) is not int):# jesli peavda to funkce ukoncena
        return "Jaden ze argumentu neni cele cislo"
    
    if a >=b:
        return f"{a} vice nebo rovna se {b}"
    return f"{a} mene {b}"
print(nums_info(True, 10))# Jaden ze argumentu neni cele cislo

print(nums_info(10, 2))# 10 vice nebo rovna se 2

print(nums_info(4, 15 ))# 4 mene 15'''


# if elif else ve funkci
'''def nums_info(a, b):
    if(type(a) is not int) or (type(b) is not int):# jesli peavda to funkce ukoncena
        info = "Jaden ze argumentu neni cele cislo"
    elif a >=b:
        info = f"{a} vice nebo rovna se {b}"
    else:
        info = f"{a} mene {b}"
    return(info)

print(nums_info(True, 10))# Jaden ze argumentu neni cele cislo

print(nums_info(10, 2))# 10 vice nebo rovna se 2

print(nums_info(4, 15 ))# 4 mene 15'''

# ukol if

'''def route_info(info):
    if ('distance' in info) and type(info['distance']) is int:
        return f"Distance to your destination is  {info['distance']}"
    if 'speed' and 'time' in info:
        return f"Distance to your destination is {info['speed'] * info['time']}"
    
    return "No distance info is available"
  

print(route_info({'distance': 200}))
#Distance to your destination is  200

print(route_info({'speed': 200, 'time': 60}))
#Distance to your destination is 12000

print(route_info({'speed': 200}))
# No distance info is available'''

# ternalni operator
# tak
'''my_number = 21.5
print("is in") if type(my_number) is int else print("is not int")'''
# nebo tak
'''if type(my_number) is int:
    print("is int")
else:
    print("is not int")'''
# if else z volanim funkce
'''send_img(img) if img.get['is_processed'] else process_and_send_img(img)'''
# kontrola exist product
'''product_qty = 10 
print("in stock" if product_qty > 0 else "out of stock")'''

# ternalni operator
'''my_img = ('1920', '1080')

# 1920x1080
print(f"{my_img[0]}x{my_img[1]}") if len(
    my_img) == 2 else print("Incorrect image formatting")

info = f"{my_img[0]}x{my_img[1]}" if len(
    my_img) == 2 else "Incorrect image formatting"


print(info)

if len(my_img) == 2:
    info = (f"{my_img[0]}x{my_img[1]}")
else:
    info = ("Incorrect image formatting")
    print(info)


my_imp = "Incorrect, Incorrect, Incorrect, Incorrect, 
Incorrect, Incorrect, Incorrect, Incorrect, Incorrect"
print("string is shirt") if len(my_imp) < 79
 else print("string is long")'''

# cykly
# for while

# ukol

# konvertujem dict v list tuplu(seznam taplu) i
# jesli hodnota klice je cele cislo mnozime na  2


'''def dict_to_list(my_dict):
    list_for_convertion = []

    for k, v in my_dict.items():

        if type(v) == int:
            v *= 2
        list_for_convertion.append((k, v))

    return list_for_convertion

print(dict_to_list({'name': 20, 'comments_qty': 23.5, 'pop': 5}))'''

#zkraceny cykl for

'''all_nums = [-3, 1, 0, 10, -20, 5]

absolute_nums = [] # znamena ze cisla jsou pozitivni bez -
for num in all_nums:
    absolute_nums.append(abs(num))

print(absolute_nums)

absolute_nums = [abs(num) for num in all_nums] 
print(absolute_nums)
print(all_nums) # puvodni list bez zmen'''
# oba varianty spravne

'''all_nums = [-3, 1, 0, 10, -20, 5]
positive_nums = []

# obycejny cykl for
for num in all_nums:
    if num > 0:
        positive_nums.append(num)

print(positive_nums)

# zkraceny cykl for 
positive_nums = [num for num in all_nums if num > 0]
print(positive_nums)'''

 # novy set  gde  kazdy element mnozime na sebe
 # for 
'''my_set = {1, 10, 15}
new_set = set() # vytvorime novy set

for val in my_set: # prochazime set kazdy element
    new_set.add(val*val) # a pridame kazdy element postupne do 
                         # noveho setu pri tom mnozime na sebe
print(new_set)'''
#zkraceny cykl
'''my_set = {1, 10, 15}
new_set = {val *val for val in my_set}
print(new_set)'''

# for
'''my_score ={
    'a': 10,
    'b': 7,
    'm': 14,
}

scores = {}

for key, value in my_score.items():
    scores[key] = value * 10

print(scores)
# zkracena for in
scores = {k: v *10 for k, v in my_score.items()}
print(scores)'''

# set z slovniku
'''
my_score ={
    'a': 10,
    'b': 7,
    'm': 14,
}
scores = {v * 10 for k, v in my_score.items()}
print(scores) # {140, 100, 70}
'''
# list z slovniku

'''my_score ={
    'a': 10,
    'b': 7,
    'm': 14,
}
scores = [v * 10 for k, v in my_score.items()]
print(scores)'''
# slovnik z lista
'''my_score = [10, 7, 14]

scores = {index: elem for index, elem in enumerate(my_score)}
print(scores)'''
# ukol novy slovnik ze slovnika gde  hodnota klicu bude  upper
'''my_dict = {
    1: 'bmw',
    2: 'skoda',
    3: 'audi',
    4: 'apple',
}
my_new_dict = {k: v.upper() for k , v in my_dict.items()}
print(my_new_dict)'''
# ukol novy list v kterem zustanou pouze vetsi nez 3
'''my_list = ['bmv', 'motorrbike', 'wv', 'audi']'''
# zkraceny fot in
'''my_newlist = [x for x in my_list if len(x) > 3]
print(my_newlist)'''

# funkce filter
'''my_newlist = filter (lambda x: len(x) > 3 , my_list)
print(list(my_newlist))'''

