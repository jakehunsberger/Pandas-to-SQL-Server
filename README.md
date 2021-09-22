# Pandas-to-SQL-Server
Insert your pandas DataFrame into existing table in a SQL Server database

There is only one function "Insert_DataFrame()" which takes 4 arguments. The first is your Pandas DataFrame. The second is your table name in the SQL Sever database.
The third is your SQL Server database connection object. The fourth is your connection's cursor object. The connection and cursor objects can be obtained from the
pyodbc Python library.

The function works by building up programmatically building up a SQL statement which exists in Python as a string object. All values in the Pandas DataFrame will be
inserted into the SQL Server table when running the function. All column names in the Pandas DataFrame must therefore exist as column names in the SQL Server table.
However, not all columns in the SQL Server table need to be populated in the Pandas DataFrame. There are only 4 acceptable data types: 
numpy.int64, numpy.float64, string (Python native) and Pandas Timestamp (pandas._libs.tslibs.timestamps.Timestamp).


