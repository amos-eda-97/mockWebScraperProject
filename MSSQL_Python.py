import pymssql
def connectToDb():
    server = '185.136.157.12'
    user = 'mqttuser'
    paswd = '@5TdXk-XzN?PRd$M'
    database = 'mqtt'
    conn = pymssql.connect(server, user, paswd, database)
    return [conn.cursor(),conn]
def getColumns(cursor,conn,table_name):
    cursor.execute("SELECT * FROM	INFORMATION_SCHEMA.COLUMNS where TABLE_NAME = 'sampleTable1'")
    rows = cursor.fetchall()
    return [i[3] for i in rows]
def getTopThouRows(cursor):
    cursor.execute("select top(1000) * from sampleTable1")
    rows = cursor.fetchall()
    return rows
cursor,conn = connectToDb()
# print(cursor,conn)
#Get columns 
col_list= getColumns(cursor,conn,"FK_ProductID")
entries = getTopThouRows(cursor)
#Get index of FK_ProductID
indexOfCol = col_list.index("FK_ProductID")
print([i[indexOfCol] for i in entries])
# print("Index ", col_list.index("FK_ProductID"))

# print(getColumns(cursor,conn,"FK_ProductID"))
