import sys
import pyodbc 
import sql_repo




# Passed variables via batch file in jenkins
if sys.argv:
    dataprovider = int(sys.argv[0])
    test_server = sys.argv[1]  # Populate for testing in QA

# Connection string to system_dataprovider to obtain destination information
conn_string_dpid = "Driver={SQL Server};Server=popdbprocman;<database name>;Trusted_Connection=yes;"

# This is a standard sql statement 
dpid_select_sql = f"SELECT clientServer, clientDB FROM <table name> WHERE clientID = {Client}" 

#Execute sql to obtain destination information
with pyodbc.connect(conn_string_dpid) as conn_select:
    cursor = conn_select.cursor()
    cursor.execute(dpid_select_sql)
    data = cursor.fetchall()

if <clientID> == 1234:
    select_sql = sql_repo.select_sql_1234
else:
    exit("Dataprovider not configured")
    

if test_server is None:
    server = data[0][0]
    database = data[0][1]
    destination_server = "server_name"
else:
    server = data[0][0]
    database = data[0][1]
    destination_server = test_server    

print(f"Using: {destination_server} as insert destination\n")
conn_string_select = f"Driver={{SQL Server}};Server={server};Database={database};Trusted_Connection=yes;"
conn_string_insert = f"Driver={{SQL Server}};Server={destination_server};Database=<db name>;Trusted_Connection=yes;"    


# Create connection to database and executes select sql - connection will close automatcially 
with pyodbc.connect(conn_string_select) as conn_select:
    cursor = conn_select.cursor()
    cursor.execute(select_sql)
    data = cursor.fetchall()
   
print("Aid codes to be inserted **ProductID not yet generated**\n")
# Verify data
for row in data:
    print(row) 


# Create connection to database and executes insert sql - connection will close automatcially 
with pyodbc.connect(conn_string_insert) as conn_insert:
    cursor = conn_insert.cursor()
    cursor.executemany(sql_repo.check_sql ,data)
    data_i = cursor.fetchall()
    if  len(data_i) > 0:
        exit("\nAid codes already exist")          
    else:
        print("Inserting aid codes")
        cursor.executemany(sql_repo.insert_sql, data)
