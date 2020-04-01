import pymysql
import datetime

# Create a connection object
dbServerName    = "127.0.0.1"
port = 8889
dbUser          = "root"
dbPassword      = ""
dbName          = "blog_flask"
# charSet         = "utf8mb4"

conn   = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword,db=dbName, port= port)
try:
    # Create a cursor object
    cursor = conn.cursor()
    
    # Insert rows into the MySQL Table 
    now = datetime.datetime.utcnow()
    my_datetime = now.strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('INSERT INTO posts (post_id, post_title, post_content, \
    filename,post_time) VALUES (%s,%s,%s,%s,%s)',(5,'title2','description2','filename2',my_datetime))
    conn.commit()
    
except Exception as e:
    print("Exeception occured:{}".format(e))

finally:
    conn.close()