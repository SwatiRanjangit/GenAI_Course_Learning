'''
stemming is the process of reducing the word stem that affix to suffix and prefix or to the roots of words known as lemma.


Drawback of stemming:
1. it does give wrong word for some words hence it is not that much efficient.
2. but in classification items, spam mails check we should go for stemmming                                                                                                                  

words=['eating','eat','eaten','writing','writes','written','programming','programs','history']

from nltk.stem import PorterStemmer

stemming = PorterStemmer()

for word in words:
    print(word+"--->"+stemming.stem(word))
 '''   
'''
RegexStemmer class:
provide regular expression and then do stemming.



from nltk.stem import RegexpStemmer

reg_stemmer=RegexpStemmer('ing$|s$|e$|able$',min=4)

print(reg_stemmer.stem('eating')) # it will match with all the regular expression like in regular expression there is a word last with ing should remove ing and give other word as output
print(reg_stemmer.stem('writing'))
print(reg_stemmer.stem('disable'))

'''

'''
Snowball stemmer:
better than porterstemmer.
better accurecy than porterstemmer
'''
from nltk.stem import SnowballStemmer
words=['eating','eat','eaten','writing','writes','written','programming','programs','history','finally','finalized','fairly','sportingly']
snowballstemmer=SnowballStemmer('english')

for word in words:
    print(word+'--->'+snowballstemmer.stem(word))