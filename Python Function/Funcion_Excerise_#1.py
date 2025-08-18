def differences(a,b):
    return a - b
print(differences(2, 2))
print(differences(0, 2))


days_of_week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
day_numbers = (1,2,3,4,5,6,7)


my_dict = {num: value for num, value in zip(day_numbers, days_of_week)}
def print_day(num):
    if num in my_dict:
        return my_dict[num]
    else:
        return None   
print(print_day(4))  
print(print_day(41)) 


def last_element(my_list):
    if my_list:
        return my_list[-1]
    return None
print(last_element([1,2,3,4]))
print(last_element([]))


def number_compare(a,b):
    if a > b:
        return "First is greater"
    elif a < b:
        return "Second is greater"
    else:
        return "Numbers are equal"
print(number_compare(1,1))
print(number_compare(1,2)) 
print(number_compare(2,1))


def count_letter(word, letter):
    return word.lower().count(letter.lower())
print(count_letter('amazing','A'))


def multiple_letter_count(string_input):
    myy_dict = {}
    for letter in string_input:
        myy_dict[letter] = string_input.count(letter)
    return myy_dict
print(multiple_letter_count("hello"))
print(multiple_letter_count("person"))


def list_manipulation (my_list, command, location, value=None):
    if command == "remove":
        if location == "end":
            return my_list.pop()
        elif location == "beginning":
            return my_list.pop(0)
        
    if command == "add":
        if location == "end":
            my_list.append(value)
            return my_list
        elif location == "beginning":
            my_list.insert(0, value)
        return my_list
print(list_manipulation([1,2,3], "remove", "end"))
print(list_manipulation([1,2,3], "remove", "beginning"))
print(list_manipulation([1,2,3], "add", "beginning", 20))
print(list_manipulation([1,2,3], "add", "end", 30))


def is_palindrome(word):
    cleaned = word.replace(" ", "").lower()
    reversed_text = cleaned[::-1]
    return cleaned == reversed_text
print(is_palindrome('testing'))
print(is_palindrome('tacocat')) 
print(is_palindrome('hannah'))
print(is_palindrome('robert')) 

def frequency(my_list, search_term):
    return my_list.count(search_term)
print(frequency([1,2,3,4,4,4], 4))
print(frequency([True, False, True, True], False))


def flip_case(string, letter):
    result = ""
    for char in string:
        if char.lower() == letter.lower():
            if char.isupper():
                result += char.lower()
            else: 
                result += char.upper()
        else: 
            result += char 
    return result
print(flip_case("Hardy har har", "h"))
                            

def multiply_even_numbers(numbers):
    product = 1 
    for num in numbers:
        if num % 2 == 0:
            product *= num 
    return product 
print(multiply_even_numbers([2,3,4,5,6]))

def mode (nums):
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0 ) +1 
    return max(counts, key=counts.get)
    
print(mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4])) 

def capitalize(word):
    return word.capitalize()
print(capitalize("tim"))  
print(capitalize("matt")) 

def compact(lst):
    return [val for val in lst if val]
print(compact([0,1,2,"",[], False, {}, None, "All done"]))


def partition(my_list, callback):
    true_list = []
    false_list = []
    for item in my_list:
        if callback(item):
            true_list.append(item)
        else:
            false_list.append(item)
    return ([true_list, false_list])

def is_even(num):
    return num % 2 == 0
print(partition([1,2,3,4], is_even))


def intersection(list1, list2):
    result = []
    for item in list1:
        if item in list2:
            result.append(item)
    return result
print(intersection([1,2,3], [2,3,4]))       


def once(fn):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return fn(*args, **kwargs)
        return None
    wrapper.has_run = False
    return wrapper

def add(a, b):
   return a + b

one_addition = once(add)

print(one_addition(2,2)) 
print(one_addition(2,2))
print(one_addition(12,200))


def run_once(fn):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return fn(*args, **kwargs)
        return None
    wrapper.has_run = False
    return wrapper

@run_once
def add(a, b):
   return a + b

print(add(2,2)) 
print(add(2,20))
print(add(12,20))


    
    
        
