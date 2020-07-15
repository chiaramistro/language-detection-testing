import MySQLdb
import json

"""
Script for the creation of the upload_content JSON file
"""

#select start and end date of the time interval
#for testing:
    #startDate/endDate: 2019-01-01 gives 4 contents back
    #startDate: 2019-01-01 endDate: 2019-01-02 gives 1111 contents back (use LIMIT in sql)
    #startDate: 2019-01-01 endDate: 2019-01-09 gives 10035 contents back

startDate = '2019-01-01'
endDate = '2019-01-09'
rows = '10000'

#create Content object to store all data about each content
class Content(object):
    associated_customers=[]
    date= ""
    headlines= ""
    id=0
    page=""
    source_id=""
    source_language= ""
    subhead=""
    subtitle= ""
    text=""
    title= ""
    type= ""

def make_content(associated_customers, date, headlines, id, page, source_id, source_language, subhead, subtitle, text, title, type):
    content = Content()
    content.associated_customers =  associated_customers
    content.date = date
    content.headlines = headlines
    content.id = id
    content.page = page
    content.source_id = source_id
    content.source_language = source_language
    content.subhead = subhead
    content.subtitle = subtitle
    content.text = text
    content.title = title
    content.type = type
    return content

#list to store all the contents
listOfContents = []

def createJSONFile():
    #open database connection
    db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="",db="recommender_db")
    cursor = db.cursor()

    #create and execute query to retrieve overall data
    #sql = 'select date, headlines, content_id as id, page, source_id, source_language, subhead, subtitle, text, title, type from content where date between \''+startDate+'\' and \''+endDate+'\';'
    sql = 'select date, headlines, content_id as id, page, source_id, source_language, subhead, subtitle, text, title, type from content where date between \''+startDate+'\' and \''+endDate+'\' limit '+rows+';'
    cursor.execute(sql)
    all_rows = cursor.fetchall()
    #print("Returned %d rows" % len(all_rows))
    for row in all_rows:
        content = make_content([], row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
        listOfContents.append(content)

    #create and execute query to retrieve associated customers for each content
    for content in listOfContents:
        sql = 'select customer_id from current_system_association where content_id ='+str(content.id)+';'
        associatedCustomers = []
        cursor.execute(sql)
        all_rows = cursor.fetchall()
        for row in all_rows:
            associatedCustomers.append(row[0])
        content.associated_customers = associatedCustomers

    #close db connection
    cursor.close()
    db.close()

    #write data in the json file
    data = []
    for content in listOfContents:
        data.append({
    'associated_customers': content.associated_customers,
    'date': str(content.date),
    'headlines': content.headlines,
    'id': content.id,
    'page': content.page,
    'source_id': content.source_id,
    'source_language': content.source_language,
    'subhead': content.subhead,
    'subtitle': content.subtitle,
    'text': content.text,
    'title': content.title,
    'type': content.type
    })

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
