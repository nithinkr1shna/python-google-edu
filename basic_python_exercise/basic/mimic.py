#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys


def create_word_list(filename):
	with open(filename, 'r') as f:
		word_string = f.read().replace('\n', " ")
	return word_string.split()

def mimic_dict(filename):
	word_list = create_word_list(filename)
	word_dict = {}
	count = 0
	word_dict[""] = word_list
	length = len(word_list)
	while length > 0:
		if word_list[count] not in word_dict:
			if count + 1 > length:
				break
			word_dict[word_list[count]] = list()
			word_dict[word_list[count]].append(word_list[count+1])
		else:
			if count + 1> length:
				break
			word_dict[word_list[count]].append(word_list[count+1])
		#print word_dict
		length -=1
		if count+1 >length:
			break
		else:
			count +=1

	return word_dict

def get_random(dict, key):
	"""Get random word correspondig to a key"""
	try:
		probable_words = dict[key]
		return random.choice(probable_words)
	except KeyError:
		return random.choice(dict[""])

def print_mimic(mimic_dict, word):
  """Given mimic dict and start word, prints 200 random words."""
  # +++your code here+++
  str = ""
  for i in xrange(1,201):
  	first = get_random(mimic_dict, word)
  	prev = get_random(mimic_dict, first)
  	str = str+" " +first+" "+prev
  	first = prev


  print  str


# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print 'usage: ./mimic.py file-to-read'
    sys.exit(1)
  
  #print mimic_dict(sys.argv[1])
  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


if __name__ == '__main__':
  main()
