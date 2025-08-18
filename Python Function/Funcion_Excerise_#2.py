def reverse_string(text):
    return text[::-1]
print(reverse_string("world"))
print(reverse_string("word"))


def new_avg(arr, target_avg):
    current_sum = sum(arr)
    count = len(arr)

    x = target_avg * (count +1) - current_sum

    if x <=0:
        raise ValueError("Expeced donation must be positive")
    
    return int(x)
print(new_avg([14, 30, 5, 7, 9, 11, 15], 92))
print(new_avg([14, 30, 5, 7, 9, 11, 15], 2)) 


def sequence_sum(begin, end, step):
    if begin > end:
        return 0
    total = 0
    for i in range(begin, end  + 1, step):
        total += i
    return total  
print(sequence_sum(2,2,2))
print(sequence_sum(2,6,2))
print(sequence_sum(1,5,1))
print(sequence_sum(1,5,3))

def max_diff(lst):
    if len(lst) <=1:
        return 0
    largest = max(lst)
    smallest = min(lst)
    return largest - smallest 
print(max_diff([1, 2, 3, 4]))
print(max_diff([1, 2, 3, -4]))  


def countSmileys(arr):
    count = 0
    for face in arr:
        if len(face) == 2:   # eyes + mouth
            if face[0] in [':', ';'] and face[1] in [')', 'D']:
                count += 1
        elif len(face) == 3:  # eyes + nose + mouth
            if face[0] in [':', ';'] and face[1] in ['-', '~'] and face[2] in [')', 'D']:
                count += 1
    return count
print(countSmileys([':)', ';(', ';}', ':-D']))      
print(countSmileys([';D', ':-(', ':-)', ';~)']))    
print(countSmileys([';]', ':[', ';*', ':$', ';-D'])) 
print(countSmileys([]))                             


def sentence_count(paragraph):
    count = 0
    for char in paragraph:
        if char in ".!?":
            count += 1
    return count

# print(sentence_count("Hello! How are you doing? I am fine."))
# print(sentence_count("No punctuation here"))
# print(sentence_count("Wow! Really? Yes."))

def race(v1, v2, g):
    if v1 >= v2:
        return None  

    time_seconds = g * 3600 // (v2 - v1)

    hours = time_seconds // 3600
    minutes = (time_seconds % 3600) // 60
    seconds = time_seconds % 60

    return [hours, minutes, seconds]


print(race(720, 850, 70))  # [0, 3
print(race(80, 91, 37))    # [3, 21, 49]
print(race(820, 81, 550))  # None


def shifted_diff(s1, s2):
    if len(s1) != len(s2):
        return -1
    if s1 == s2:
        return 0
    pos = (s2 + s2).find(s1)   
    return pos if pos != -1 else -1



print(shifted_diff("coffee", "eecoff")) 
print(shifted_diff("eecoff", "coffee")) 
print(shifted_diff("moose", "Moose"))    
print(shifted_diff("isn't", "'tisn"))   
print(shifted_diff("Esham", "Esham"))   
print(shifted_diff("dog", "god"))       


