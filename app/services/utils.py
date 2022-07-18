from attr import NOTHING
import psycopg2
from psycopg2 import sql
import sys

try:
    conn = psycopg2.connect(
        host='ec2-3-219-229-143.compute-1.amazonaws.com', 
        database='dhi2fhbdcpk81',
        user='tudjloatajaahd',
        password='77b778d73f1ec79b959f0b8e78cc09a5aace31d31a662f7b0e3c6b17e0f7a1b2'
    )
    cur = conn.cursor()

except:
    exit("Error: Unable to connect to the database")


def addLink(url):
    try:

        cur.execute("INSERT INTO ibm_links.links(link) values (%s)", (url,))
        conn.commit()
    except Exception as e:
        print(e)

def addLinks(linkList):
    try:
        for link in linkList:
            cur.execute("INSERT INTO ibm_links.links(link) values (%s)", (link,))
            conn.commit()
    except Exception as e:
        print(e) 

def getLinks():
    
    cur.execute("SELECT link from ibm_links.links")
    links = cur.fetchall()

    return links
    
