#2)ans:
a=[1,2,3,4,5,6,7,8,9,10]
A=list(map(lambda x:x**2,a))
print(A)

#3)ans:
given_string=[1,2,3,4,5,6,7,8,9,10]
b=tuple(map(lambda x:str(x),given_string))
print(b)

#4)ans:
nums_=list(range (1,26))
from functools import reduce
C =(reduce(lambda x,y:x * y,nums_))
print(C)
l=[2,3,6,9,27,60,90,120,55,46]
s= (list(filter(lambda x:x %2==0,l)))
print(s)
d= (list(filter(lambda x:x%3==0,l)))
print(d)

#5ans:
str_list = ['Python', 'php', 'aba', 'radar', 'level']

# Define a lambda function to check for palindromes
is_palindrome = lambda s: s.lower() == s[::-1].lower()

# Use filter to find palindromes in the list
palindromes = list(filter(is_palindrome, str_list))

# Print the result
print(palindromes)

#1)ans
# Define the list of tuples
player_stats = [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]

# Define a lambda function to extract the integer value from each tuple
get_int_value = lambda x: x[1]

# Use sorted to sort the list based on the integer value
sorted_list = sorted(player_stats, key=get_int_value, reverse=True)

# Print the sorted list
print(sorted_list)
