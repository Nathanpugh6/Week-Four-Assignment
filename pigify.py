# Nathan Pugh Collaborated with: Nicole Ignasiak, Josiah Hardacre, Trevor Waite
# CIS 125 82A
# 30 September 2015
# Week 4 Lab

vowels = "aeiouAEIOU"

# Ask for word

word = input("Please enter a word: ")

# Loop through word, one letter at a time

for letter in word:
	# Check if letter is a vowel
	if letter in vowels:
		# True?  We are done
		pig = word + "yay"
	else:
		# False? Consonant
		pig = word[1:] + word[0] + "ay"
		
print(pig)