# Aid Code Project 
The goal of creating an automated script that can scan an import table and create aid codes to be inserted into core_base. 

The code in aidcode-creator.py works as follows:

Create connection to Server to obtain client details
Create connection to Client database to obtain uncreated aid codes
Creats aid codes according to a predeifned sql statement housed in sql_repo.py
Create connection to data defeintion db and inserts new aid codes


## Adding a new feed into this code

To include a new feed into this script two files will need to be modified 1) sql_repo.py 2) aidcode-creator.py. Instructions on how to alter these files are blow.

### Sql_repo

Create a variable with the naming converting select_sql_<Dataprovider>  (replace dataprovider with the actual dataprovider number). This sql statement should have all the code to extract the desired columns and provide transformed results. These results will be used in the insert statement, the columns must be ordered in the select from left to right (ProductGroupID, ProductCode, ProductName, ProductDescription, GETDATE() as Updated). The productID will be auto incremented via insert statement.

### Aidcode-creator

Make an addition to the logic flow found starting on line 30 of the aidcode-creator.py file. Copy example lines below and paste them on line 32 preserving the existing code. Change the dataprovider numbers to corresponding to your new feed. 

Example:
if dataprovider == <Dataprovider>:
    select_sql = sql_repo.select_sql_<Dataprovider>

