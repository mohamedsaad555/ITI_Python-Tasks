#1
print("---Q1----")
def q1(length,start):
    z=[]
    for i in range(length):
          z.append(start)
          start+=1
    return z
print(q1(5,2))
#2
print("---Q2----")
def fizzbuzz(num):
	if num%3 == 0 or num%5 == 0:
		s = ''
		if num%3 == 0:
			s += 'Fizz'
		if num%5 == 0:
			s += 'Buzz'
		return s
	else:
		return num


print(fizzbuzz(3))
print(fizzbuzz(5))
print(fizzbuzz(15))
print(fizzbuzz(11))
#3
print("---Q3----")
def reverse(string):
    reverse_string = string[::-1]
    return reverse_string
print("Result: ", reverse(input("Enter Name ")))

#4
print("---Q4----")
name = input("Enter name and hit enter ")
#Email=input("Enter email and hit enter ")
print("type of text ", type(name))
#print("type of text ", type(Email))
import re
 
# Define a function for
# for validating an Email
def check(s):
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.match(pat,s):
        print("Valid Email")
    else:
        print("Invalid Email")
 
# Driver Code
if __name__ == '__main__':
 
    # Enter the email
    email = "ankitrai326@gmail.com"
 
    # calling run function
    check(email)
 
    email =input(" enter email ") 
    check(email)
 
    email = "ankitrai326.com"
    check(email)

#5
print("---Q5----")
def longest_substring(s):
    longest = ''
    current = ''

    for c in s:
        if current == '' or c >= current[-1]:
            current += c
        else:
            current = c
        longest = max(current, longest, key=len)

    return longest
print(longest_substring('helloworld'))

#6
print("---Q6----")
count = 0
total = 0
average = 0 
while True:
    numlist = input('Enter a number or press Enter to quit: ')
    if numlist == "done" :
        break
    try:
        count = count + 1
        total = total + float(numlist)
    except:
        count = count - 1
        print('error message')
        continue
average = float(total) / float(count) 
print('The sum is', total)
print('The average is', average)

#7
print("---Q7----")
import random
# library that we use in order to choose
# on random words from a list of words

name = input("What is your name? ")

# Here the user is asked to enter the name first

print("Good Luck ! ", name)

words = ['rainbow', 'computer', 'programming',
		'python',  'player', 'water', 'geeks']

# Function will choose one random
# word from this list of words
word = random.choice(words)


print("Guess the characters")

guesses = ''

# any number of turns can be used here
turns = 7


while turns > 0:

	# counts the number of times a user fails
	failed = 0

	# all characters from the input
	# word taking one at a time.
	for char in word:

		# comparing that character with
		# the character in guesses
		if char in guesses:
			print(char, end=" ")

		else:
			print("_")

			# for every failure 1 will be
			# incremented in failure
			failed += 1

	if failed == 0:
		# user will win the game if failure is 0
		# and 'You Win' will be given as output
		print("correct placement")

		# this print the correct word
		print("The word is: ", word)
		break

	# if user has input the wrong alphabet then
	# it will ask user to enter another alphabet
	print()
	guess = input("guess a character:")

	# every input character will be stored in guesses
	guesses += guess

	# check input with the character in word
	if guess not in word:

		turns -= 1

		# if the character doesn’t match the word
		# then “Wrong” will be given as output
		print("guess another alphapet")

		# this will print the number of
		# turns left for the user
		print("You have", + turns, 'more guesses')

		if turns == 0:
			print("You Loose")
                        

