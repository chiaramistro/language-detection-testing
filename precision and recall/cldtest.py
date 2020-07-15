import contentCreator
import precisionAndRecall
import cld2
import time

"""
Analyze content using "cld" package
"""

def runCld():
    contentCreator.createContentList()

    print("--- Start of Cld Tool ---")
    start_time = time.time()

    for content in contentCreator.listOfContents:
        concat = content.title+" "+content.text
        isReliable, textBytesFound, details = cld2.detect(concat)
        # Example of details: (('ENGLISH', 'en', 95, 1736.0), ('Unknown', 'un', 0, 0.0), ('Unknown', 'un', 0, 0.0))

        lang = details[0][1]
        #normalization possible by dividing percentage / 100
        prob = (details[0][2])/100
        #print("Text title %s - language %s - probability %f" % (content.title, lang , prob))
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

    print("--- End of Cld Tool ---")
    execTime = (time.time() - start_time)
    print("--- To detect languages for %s: %s seconds ---" % (analyzedLanguage, execTime))
