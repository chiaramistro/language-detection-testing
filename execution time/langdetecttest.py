import updatecontent
from langdetect import detect
import time

"""
Language detect package "langdetect" test
"""

start_time = time.time()
updatecontent.createJSONFile()
print("--- To create JSON FILE: %s seconds ---" % (time.time() - start_time))


start_time = time.time()

for content in script.listOfContents:
    print("Text with title %s is in language %s" % (content.title, detect(content.text)))

print("--- To detect language: %s seconds ---" % (time.time() - start_time))
