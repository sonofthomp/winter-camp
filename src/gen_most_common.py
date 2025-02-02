'''
PART 3:
 - Generating a dictionary of most-common capitalizations based on 

CL args:
  1. Training tokens file (should end in .tok)
  2. JSON file that will contain the most common capitalizations of words (should end in .json)
'''

from collections import Counter
from sys import argv
import json

def gen_most_common():
	with open(argv[1], 'r') as in_file:
		words = in_file.read().split(' ')

	# Keys are words, vals are counters of casings of the word
	case_counter = {}

	# Update casing counter for each word
	for word in words:
		if not(word.lower() in case_counter):
			case_counter[word.lower()] = Counter()

		case_counter[word.lower()][word] += 1

	# Find track of the most common casing of every word, store it in most_common
	most_common = {}
	
	for lower in case_counter.keys():
		most_common[lower] = case_counter[lower].most_common()[0][0]

	# JSONify and dump most_common
	with open(argv[2], 'w') as out_file:
		out_file.write(json.dumps(most_common, indent=4))

gen_most_common()