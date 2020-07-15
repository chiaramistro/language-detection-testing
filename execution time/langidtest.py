import updatecontent
import langid
import time

"""
Language detect package "langid" test
"""

start_time = time.time()
updatecontent.createJSONFile()
print("--- To create JSON FILE: %s seconds ---" % (time.time() - start_time))


start_time = time.time()

for content in script.listOfContents:
    #select the first element since it returns a tuple with language and precision
    print("Text with title %s is in language %s" % (content.title, langid.classify(content.text)[0]))

print("--- To detect language: %s seconds ---" % (time.time() - start_time))
