my_list = [1, 2, 3, 4]
print([x for x in my_list])

my_listt = [2, 4, 5,]
print([x * 20 for x in my_listt])

names = ['Elie', 'Tim', 'Matt']
first_letters = [name[0] for name in names]
print(first_letters)   

nums = [1, 2, 3, 4, 5, 6]
even_nums = [x for x in nums if x % 2 == 0]
print(even_nums)

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

intersection = [x for x in list1 if x in list2]
print(intersection)

words = ["Elie", "Tim", "Matt"]

result = [word.lower()[::-1] for word in words]
print(result)

word1 = "first"
word2 = "third"

result = [letter for letter in word1 if letter in word2]
print(result) 

result = [x for x in range(1, 101) if x % 12 == 0]
print(result)

word = "amazing"
vowels = ['a', 'e', 'i', 'o', 'u']

result = [letter for letter in word if letter not in vowels]
print(result) 

result = [[0, 1, 2] for _ in range(3)]
print(result)

result = [[x for x in range(10)] for _ in range(10)]
print(result)