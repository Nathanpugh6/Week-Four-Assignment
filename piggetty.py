# Nathan Pugh Collaborated with: Nicole Ignasiak, Josiah Hardacre, Trevor Waite
# CIS 125 82A
# 30 September 2015
# Week 4 Lab

# Magic Happens Here
# pig = word
# Ignore previous line
	
# return pig

# Open the file *getty.txt* for reading.  

gettyfile = open("getty.txt", "r")

# Open a new file *piggy.txt* for writing.  
piggyfile = open("piggy.txt", "w")

# Read the getty.txt file into a string.  
address = gettyfile.read()

# Strip out bad characters (, - .).  
address = address.replace(".","")
address = address.replace(",","")
address = address.replace("-","")

print(address)

# Define a function called piggy(string) that returns a string
def piggy():
# Split the string into a list of words.  
	listaddress = address.split()

# Create a new empty string.  
	piggystring = ""

# Loop through the list of words, pigifying each one.  
	vowels = "aeiouAEIOU"
	piggynewword = ""

# Goes through every word in Gettysburg Address
	for word in listaddress:
	
# Checking every first letter of the word and changes to pig latin
		if word[0] in vowels:
			piggynewword = (word + "yay")
		
# Adding every changed word along with a space between words to new string
			piggystring = piggystring + " " + piggynewword
		else:
			n=0
			for letter in word:
				if letter in vowels:
					piggynewword = (word[n:] + word[0:n] + "ay")
					piggystring = piggystring + " " + piggynewword
					break
				n+=1
	return piggystring
	
finalpiggystring = piggy()
# Write the new string to piggy.txt.  
piggyfile.write(finalpiggystring)

# close the files.
piggyfile.close()
gettyfile.close()