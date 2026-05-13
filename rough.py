# import math
# def factorial(n):

#     return math.factorial(n)
# print(factorial(500))
# def is_prime(n):
#     if n<2 :
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n%i ==0:
#             return False
        
#     return True
# # print(is_prime(7))
# PRIME_NUMBERS = [x for x in range(500) if is_prime(x)]
# print(PRIME_NUMBERS)


# #anagram?
# def is_anagram(str1, str2):
#     str1 = str1.replace(" ","").lower()
#     str2 = str2.replace(" ","").lower()
#     if len(str1) != len(str2):
#         return False
#     return sorted(str1) == sorted(str2)
# # # Testing the code
# # print(is_anagram("listen", "silent"))  # Output: True
# # print(is_anagram("python", "typhon"))  # Output: True
# # print(is_anagram("hello", "world"))    # Output: False
# print(is_anagram("Debit Card", "Bad Credit"))


# k = [1,2,3,4,5,6]
# rl = 4
# results = k[rl:] + k[:rl]
# print(results)


# Example: In colors = ['red', 'green', 'blue', 'yellow'], replace ['green', 'blue'] with ['pink', 'purple', 'orange'] using slice assignment.
# colors = ['red', 'green', 'blue', 'yellow']
# replace = ['pink', 'purple', 'orange']
# colors[1:3] =replace
# # print(colors)

# new_colors = colors[:]
# print(new_colors)
# print(new_colors[::3])
# print(new_colors[-2:])
# print(new_colors[:-2])
# print(new_colors[::-1])
# print(new_colors[:])


# def max_number(numbers):
#     max_num = numbers[0]
#     for n in numbers:
#         if n>max_num:
#             max_num = n
#     return max_num
# print(max_number([10,24,5,62,11]))
# # print(max_number)



# def count_vowels(sentence):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in sentence:
#         if char in vowels:
#             count +=1
#     return count
# print(count_vowels("hello world"))

# def char_check(sentence):
#     in_sentence = "anil reddy mokalla"
#     for char in sentence:
#         if char in in_sentence:
#             return True
#     return False
# print(char_check("z"))
def reverser_string(string):
        
    reverse = ""
    for char in string:
        reverse = char + reverse
    return reverse
print(reverser_string("anilreddy"))
# string = "anilreddy"
