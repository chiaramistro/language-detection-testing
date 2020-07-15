import contentCreator
import precisionAndRecall
from langdetect import detect_langs
import re

"""
Analyze content using "langdetect" package

** Modify variable "analyzedLanguage" to analyze a specific language

"""


def runLangDetect():
    contentCreator.createContentList()

    print("--- Start of Langdetect Tool ---")
    #probability is already normalized

    for content in contentCreator.listOfContents:
        concat = content.title+" "+content.text
        array=detect_langs(concat)
        firstLang = str(array[0])
        lang = re.findall("[a-z]+", firstLang)[0]
        prob = re.findall("[0-9]\.[0-9]+", firstLang)[0]
        #print("Text title %s - language %s - probability %f" % (content.title, lang , prob))
        #save the probability and the language recognized for each content
        if (lang=='it'):
            content.recognized_language ='it_IT'
        if (lang=='de'):
            content.recognized_language ='de_DE'
        content.language_probability = float(prob)

    print("--- All documents classified ---")
    print("------------------------------------------------")
    analyzedLanguage= 'it_IT'
    #analyzedLanguage= 'de_DE'
    precisionAndRecall.getPrecisionAndRecall(analyzedLanguage, contentCreator.listOfContents)

    print("--- End of Langdetect Tool ---")
