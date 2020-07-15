import MySQLdb

"""
Script to create contents from database
"""

#create Content object to store all data about each content
class Content(object):
    content_id=0
    source_id=""
    language=""
    source_language= ""
    title= ""
    text=""
    date=""
    type=""
    recognized_language=""
    language_probability=0

def make_content(content_id, source_id, language, source_language, title, text, date, type):
    content = Content()
    content.content_id = content_id
    content.source_id = source_id
    content.language = language
    content.source_language = source_language
    content.title = title
    content.text = text
    content.date = date
    content.type = type
    return content

listOfContents = []
germanContents=[]
italianContents=[]
otherContents=[]

def createContentList():
    print("--- Create content list ---")
    #open database connection
    db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="",db="recommender_db")
    cursor = db.cursor()
    #test query limiting to 5 contents
    #select content_id, source_id, language, source_language, title, text, date, type from sample_content;
    sql = 'select content_id, source_id, language, source_language, title, text, date, type from sample_content;'
    cursor.execute(sql)
    all_rows = cursor.fetchall()
    #print("Number of rows is %d" % (len(all_rows)))
    for row in all_rows:
        #create list of contents from db
        content = make_content(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        listOfContents.append(content)
    """
    #divide german and italian contents into two lists for testing
    for content in listOfContents:
        if (content.language == "de_DE"):
            germanContents.append(content)
        elif(content.language=="it_IT"):
            italianContents.append(content)
        else:
            otherContents.append(content)

    print("There are %d German contents" % (len(germanContents)))
    print("There are %d Italian contents" % (len(italianContents)))
    print("There are %d contents of other languages" % (len(otherContents)))
    """
    #close db connection
    cursor.close()
    db.close()
    print("--- Content list is ready ---")
