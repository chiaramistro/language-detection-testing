import contentCreator
import precisionAndRecall
import langid
from langid.langid import LanguageIdentifier, model

"""
Analyze content using "langid" package

** Modify variable "analyzedLanguage" to analyze a specific language

"""

def runLangId():
    contentCreator.createContentList()

    print("--- Start of Langid Tool ---")
    #normalization of probability of match
    identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)

    for content in contentCreator.listOfContents:
        concat = content.title+" "+content.text
        lang=identifier.classify(concat)[0]
        prob=identifier.classify(concat)[1]
        #print("Text title %s - language %s - probability %f" % (content.title, lang,prob))
        #save the probability and the language recognized for each content
        if (lang=='it'):
            content.recognized_language ='it_IT'
        if (lang=='de'):
            content.recognized_language ='de_DE'
        content.language_probability =prob

    print("--- All documents classified ---")
    print("------------------------------------------------")
    #analyzedLanguage= 'it_IT'
    analyzedLanguage= 'de_DE'
    precisionAndRecall.getPrecisionAndRecall(analyzedLanguage, contentCreator.listOfContents)

    print("--- End of Langid Tool ---")
