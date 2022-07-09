import psycopg2
from psycopg2 import sql
import sys

try:
    conn = psycopg2.connect(
        host='162.214.126.100', 
        database='wwceva_logistics_latam',
        user='ceva',
        password='ivjAS@pst235240'
    )
    cur = conn.cursor()

except:
    exit("Error: Unable to connect to the database")


def addLink(url):

    cur.execute("INSERT INTO test.links(link) values (%s)", (url,))
    conn.commit()

def getLinks():
    
    cur.execute("SELECT * from test.links")
    links = cur.fetchall()

    return links
    
