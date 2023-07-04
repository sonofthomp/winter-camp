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

def extract(tokens):
    num_tokens = len(tokens)
    features = [[] for i in range(num_tokens)]
    
    for index, token in enumerate(tokens):
        casing = str(case.get_tc(token)[0])
        features[index].append(casing)
        features[index].append(f't[0]={token.lower()}')
        
        if index == 0:
            features[index].append('__BOS__')
        elif index == num_tokens - 1:
            features[index].append('__EOS__')
        
        if (index >= 1) and (index < num_tokens - 1):
            features[index].append(f't[-1]={tokens[index-1].lower()}')
            features[index].append(f't[+1]={tokens[index+1].lower()}')
            features[index].append(f't[-1]={tokens[index-1].lower()}^t[+1]={tokens[index+1].lower()}')
        
        if (index >= 2) and (index < num_tokens - 2):
            features[index].append(f't[-2]={tokens[index-2].lower()}')
            features[index].append(f't[+2]={tokens[index+2].lower()}')
            
        if len(token) > 1:
            features[index].append(f'suf1={token[-1].lower()}')
        if len(token) > 2:
            features[index].append(f'suf2={token[-2:].lower()}')
        if len(token) > 3:
            features[index].append(f'suf3={token[-3:].lower()}')
        
    return features

def gen_features(tok_filename, features_filename):
    features_file = open(features_filename, 'w')

    with open(tok_filename, 'r') as tok_file:
        lines = tok_file.readlines()

        for index, line in enumerate(lines):
            if index % 10000 == 0:
                print(index, '/', len(lines), 'lines')

            features = extract(line.strip().split())

            for token in features:
                features_file.write('\t'.join(token) + '\n')

def gen_features():
    train_out = open(argv[2], 'w')
    test_out = open(argv[4], 'w')
    dev_out = open(argv[6], 'w')

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