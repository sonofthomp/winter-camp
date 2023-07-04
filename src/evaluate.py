'''
PART 5:
 - Display percent accuracy of truecasing by comparing "golden" text and truecased text

CL args:
  1. Path to correctly capitalized tokens from the original dataset
  2. Path to truecased tokens
'''

from sys import argv
from nltk import word_tokenize

gold_path = argv[1]
predicted_path = argv[2]

gold_tokens = open(gold_path, 'r').read() # Get content of gold file
gold_tokens = gold_tokens.replace('\n', ' ').split(' ') # Split text by words and line breaks

predicted_tokens = open(predicted_path, 'r').read()
predicted_tokens = predicted_tokens.replace('\n', ' ').split(' ')

num_tokens = min(len(gold_tokens), len(predicted_tokens)) # Disregard any tokens after the length of the shorter file
total_tokens, correct_tokens = 0, 0

# Compare the casing of each token pair, keep track of # of correct tokens
for i in range(num_tokens):
	total_tokens += 1

	if gold_tokens[i] == predicted_tokens[i]:
		correct_tokens += 1

# Display accuracy
print(f'{correct_tokens} / {total_tokens} correct   |   {correct_tokens / total_tokens * 100:.6f}% accurate')