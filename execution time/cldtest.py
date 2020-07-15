import updatecontent
import time
import cld2

"""
Language detect package "cld" test
"""

start_time = time.time()
updatecontent.createJSONFile()
print("--- To create JSON FILE: %s seconds ---" % (time.time() - start_time))

start_time = time.time()

unknowns =0

for content in script.listOfContents:
    isReliable, textBytesFound, details = cld2.detect(content.text)
    # Example of details: (('ENGLISH', 'en', 95, 1736.0), ('Unknown', 'un', 0, 0.0), ('Unknown', 'un', 0, 0.0))
    #access details on [0][1] to access the language code
    print("Text with title %s is in language %s" % (content.title, details[0][1]))
    if (details[0][1] == 'un'):
        unknowns = unknowns+1
        #print("Text with title %s is in language %s" % (content.title, details[0][1]))

print("--- To detect language: %s seconds ---" % (time.time() - start_time))
print("Unknows: %d" % unknowns)
