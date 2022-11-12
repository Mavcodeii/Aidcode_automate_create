# ClientID specific AidCode creation sql 

select_sql_<clientID> = """
SELECT DISTINCT 
--a.AidCode, 
--ac.[type], 
--'x' ProductID, 
pg.ProductGroupID, 
CONCAT('Varchar','-',a.AidCode) Aid_Code, 
CONCAT(ac.[type],' - ',a.AidCode) Aid_Name, 
CONCAT(ac.[type],' - ',a.AidCode) Aid_Description, 
GETDATE() Updated
FROM <table name here> a
JOIN (
SELECT 
aid_code, 
[type] 
FROM <table name here>  a
 JOIN <table name here>  b ON a.pkid = b.pkid
 JOIN <table name here>  c ON b.fileid = c.fileid
 WHERE c.fileid = (SELECT MAX(fileid) FROM <table name here> )
) ac ON a.AidCode = ac.aid_code
JOIN <table name here>  pg ON a.datasourcename = pg.AidGroupName
LEFT JOIN <table name here>  p ON a.AidCode = RIGHT(ProductName,2) and p.AidGroupID = pg.AidGroupID
WHERE p.AidID IS NULL
"""

# Standard sql quries 

insert_sql = "INSERT INTO <table name here>  ( AidID, AidGroupID, AidCode, AidName, AidDescription, Updated) VALUES ((SELECT MAX(AidID)+1 FROM core_BASE..py_Product),?,?,?,?,?)"

check_sql = "SELECT * FROM <table name here>  WHERE AidGroupID = ? AND AidCode = ? AND AidName = ? AND AidDescription = ?"
