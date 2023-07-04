'''
PART 4:
 - Apply casing to testing .tok file according to casing predictions, and output it to a .truecased file

CL args:
  1. Tokenized testing data (should end in .tok)
  2. Testing casing predictions (should end in .predictions)
  3. Truecased output file (should end in .truecased)
'''

from case import *
from nltk import sent_tokenize
from sys import argv

with open(argv[1], 'r') as test_tokens_file:
	test_tokens = test_tokens_file.read().split()

with open(argv[2], 'r') as test_preds_file:
	test_preds = test_preds_file.read().split()

cased_words = []

for index in range(len(test_tokens)):
	uncased = test_tokens[index]
	cased = apply_tc(uncased, eval(f'TokenCase.{test_preds[index]}'))
	cased_words.append(cased)

	if index % 10000 == 0:
		print(index, '/', len(test_tokens))

cased_text = ' '.join(cased_words)

with open(argv[3], 'w') as out_file:
	out_file.write(cased_text)