'''
PART 3:
 - Generate .features files from .tok files

CL args:
  1. The training input filename (should end in .tok)
  2. The training output filename (should end in .features)
  3. The testing input filename (should end in .tok)
  4. The testing output filename (should end in .features)
  5. The development input filename (should end in .tok)
  6. The development output filename (should end in .features)
'''

from sys import argv
import case

# Generate 2d features array given a list of tokens
def extract(tokens):
    num_tokens = len(tokens)

    # This array will contain all the information about each token and its surrounding tokens
    features = [[] for i in range(num_tokens)]
    
    # For each token...
    for index, token in enumerate(tokens):
        casing = str(case.get_tc(token)[0]) # Get a casing identifier as a string
        features[index].append(casing) # Add casing identifier as first element of sublist
        features[index].append(f't[0]={token.lower()}') # Add t[0] element to sublist
        
        # Add __BOS__ or __EOS__ appropriately
        if index == 0:
            features[index].append('__BOS__')
        elif index == num_tokens - 1:
            features[index].append('__EOS__')
        
        # If we're not on an edge, add t[-1] and t[+1] and t[-1]^t[+1]
        if (index >= 1) and (index < num_tokens - 1):
            features[index].append(f't[-1]={tokens[index-1].lower()}')
            features[index].append(f't[+1]={tokens[index+1].lower()}')
            features[index].append(f't[-1]={tokens[index-1].lower()}^t[+1]={tokens[index+1].lower()}')
        
        # Ditto for t[-2], t[+2]
        if (index >= 2) and (index < num_tokens - 2):
            features[index].append(f't[-2]={tokens[index-2].lower()}')
            features[index].append(f't[+2]={tokens[index+2].lower()}')
        
        # Add last three substrings accordingly
        if len(token) > 1:
            features[index].append(f'suf1={token[-1].lower()}')
        if len(token) > 2:
            features[index].append(f'suf2={token[-2:].lower()}')
        if len(token) > 3:
            features[index].append(f'suf3={token[-3:].lower()}')
        
    return features

# Given a token file, generating a tab-separated features file of the result of extracting the text
def gen_features(tok_filename, features_filename):
    features_file = open(features_filename, 'w')

    with open(tok_filename, 'r') as tok_file:
        lines = tok_file.readlines() # Get lines of input file

        for index, line in enumerate(lines):
            # This is just so that the user can monitor progress
            if index % 10000 == 0:
                print(index, '/', len(lines), 'lines')

            # Get features of that specific sentence
            features = extract(line.strip().split())

            # Write the tab-separated features to the output file
            for token in features:
                features_file.write('\t'.join(token) + '\n')

    features_file.close()

def gen_features():
    train_out = open(argv[2], 'w')
    test_out = open(argv[4], 'w')
    dev_out = open(argv[6], 'w')

    # For training, testing, and dev data, generate and write features files
    print("GENERATING TRAIN FEATURES")
    gen_features(argv[1], argv[2])

    print("GENERATING TEST FEATURES")
    gen_features(argv[3], argv[4])

    print("GENERATING DEV FEATURES")
    gen_features(argv[5], argv[6])

    train_out.close()
    test_out.close()
    dev_out.close()

gen_features()