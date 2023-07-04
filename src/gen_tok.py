'''
PART 2:
 - Split the full corpus data into testing, training, and development .tok files (with 10%, 80%, and 10% respectively)

CL args are:
  1. The filename for the file that contains all the data
  2. The filename for where the training data should be outputted to (should end with .tok)
  3. The filename for where the development data should be outputted to (should end with .tok)
  4. The filename for where the testing data should be outputted to (should end with .tok)
'''

import random
import nltk
from sys import argv

all_data = open(argv[1], 'r')
train = open(argv[2], 'w')
dev = open(argv[3], 'w')
test = open(argv[4], 'w')

for line in all_data.readlines():
	# Tokenize each line and fix colons to conform with crfsuite
	tokens = nltk.word_tokenize(line)
	sentence = ' '.join(tokens) + '\n'
	sentence = sentence.replace(':', '_')  # replace : with _ for crfsuite

	n = random.randint(1, 10)
	if n == 1: # dev gets 10%
		dev.write(sentence)
	elif n == 2: # test gets 10%
		test.write(sentence)
	else: # train gets 80%
		train.write(sentence)

all_data.close()
train.close()
dev.close()
test.close()