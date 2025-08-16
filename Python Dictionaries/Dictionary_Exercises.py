my_list = [("name", "Elie"), ("job", "Instructor")]
my_dict = {key: value for key, value in my_list}
print(my_dict)

country_codes = ["CA", "NJ", "RI"]
states = ["California", "New Jersey", "Rhode Island"]
myy_dict = dict(zip(country_codes, states))
print(myy_dict)

vowels = ["a", "e", "i", "o", "u"]
values = [0,1,2,3,4] 
myyy_dict = {key: value for key, value in zip(vowels, values)}
print(myyy_dict)

alphabet = {i: chr(64 + i) for i in range (1, 27)}
myyyy_dict = dict(alphabet)
print(myyyy_dict)

text = "awesome sauce"
vowels = ["a", "e", "i", "o", "u"]
myyyyy_dict = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
for char in text:
    if char in vowels:
        myyyyy_dict[char] += 1
print(myyyyy_dict)