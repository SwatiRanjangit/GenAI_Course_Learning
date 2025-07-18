import nltk

'''
download issue for nltk:
python
import nltk
nltk.download('wordnet')
exit()
'''

# Download punkt tokenizer once
nltk.download('punkt')

# Sample corpus
corpus = '''Hello welcome to my world.
Hi everyone! Very good morning.
How are you today?'''


# Import the sentence tokenizer
from nltk.tokenize import sent_tokenize

# Tokenize the corpus
sentences = sent_tokenize(corpus)

# Print the tokenized sentences
#print(sentences)


from nltk import word_tokenize

#print(word_tokenize(corpus))

from nltk import wordpunct_tokenize # in this punctionas are also treated as a word

#print(wordpunct_tokenize(sentences))

from nltk import TreebankWordTokenizer

tokenizer = TreebankWordTokenizer() # it will not treate fullstop as a word.
print(tokenizer.tokenize(corpus))

