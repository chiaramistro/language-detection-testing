import updatecontent
import time
import nltk
import pycountry
from nltk.stem import SnowballStemmer

"""
Language detect package "nltk" test
"""

start_time = time.time()
updatecontent.createJSONFile()
print("--- To create JSON FILE: %s seconds ---" % (time.time() - start_time))


start_time = time.time()

tc = nltk.classify.textcat.TextCat()

for content in script.listOfContents:
    guess = tc.guess_language(content.text)
    guess_name = pycountry.languages.get(alpha_3=guess).name
    print("Text with title %s is in language %s" % (content.title, guess_name))

print("--- To detect language: %s seconds ---" % (time.time() - start_time))
