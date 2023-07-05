'''
PART 4:
 - Apply trucasing to testing .tok file according to casing predictions, output result to a .truecased file

CL args:
  1. Tokenized testing data (should end in .tok)
  2. Testing casing predictions (should end in .predictions)
  3. Truecased output file (should end in .truecased)
'''

from case import *
from nltk import sent_tokenize
from sys import argv

# Open tokens and casing predictions files
with open(argv[1], 'r') as test_tokens_file:
	test_tokens = test_tokens_file.read().split()

with open(argv[2], 'r') as test_preds_file:
	test_preds = test_preds_file.read().split()

cased_words = []

# Truecase each token according to the prediction, add all tokens to cased_words
for index in range(len(test_tokens)):
	uncased = test_tokens[index]
	cased = apply_tc(uncased, eval(f'TokenCase.{test_preds[index]}'))
	cased_words.append(cased)

	# This is just so that the user can monitor progress
	if index % 10000 == 0:
		print(index, '/', len(test_tokens))

# Format and output truecased text to output file
cased_text = ' '.join(cased_words)
with open(argv[3], 'w') as out_file:
	out_file.write(cased_text)
