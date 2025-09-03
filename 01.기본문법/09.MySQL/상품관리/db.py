import pymysql

con = pymysql.connect(
    host='localhost', #192.168.0.28
    user='root', #web
    password='1234', #pass
    db = 'shop',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor,
    port=3306
)
cur = con.cursor()