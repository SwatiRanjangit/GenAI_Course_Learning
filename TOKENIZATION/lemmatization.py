'''
it is similar to stemming.
lemmatization will give exact(meaningful) root word(correct word) known as 'lemma' rather than root stem.
it does not change the meaning.
it is better than stemming.
this uses wordNet CorpusReader to find a lemma.

it takes more time as it need to search more than stemming.
examples used: Q&A,ChatBots, text summerization
'''
''''''

from nltk.stem import WordNetLemmatizer
words=['eating','eat','eaten','writing','writes','written','programming','programs','history','finally','finalized','fairly','sportingly']

lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('going'))

print(lemmatizer.lemmatize('going',pos='v'))
print(lemmatizer.lemmatize('going','a'))
print(lemmatizer.lemmatize('going','r'))

for word in words:
    print(word+'--->'+lemmatizer.lemmatize(word,'v'))

'''
lemmatize(word,POS) takes two parameter one is word which is to be lemmatized and 2nd POS which reprents what is the word to lemmitize

POS -
Noun- n
verb- v
adjective- a
adverb- r

By default it is noun(n)
and verb is correct one.
'''