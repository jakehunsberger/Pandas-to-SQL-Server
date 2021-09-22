import pandas as pd
import numpy as np

def Insert_DataFrame(pdf, Table_Name, Connection, Cursor):
    
    #Get a list of variable names
    Column_Names = pdf.columns.tolist()
    
    #Convert variable list into string for sql query
    SQL_Var_Names_Str = '('
    for Column_Name in Column_Names:
        SQL_Var_Names_Str += Column_Name + ','
        continue
    #Replace final comma with closing parentheses
    SQL_Var_Names_Str = SQL_Var_Names_Str[:len(SQL_Var_Names_Str) - 1]
    SQL_Var_Names_Str += ')'
    
    
    #Build up value string row-by-row
    SQL_Records_Str = ''
    
    #Loop through dataframe and insert row by row
    for Record_Index in range(len(pdf)):
        
        #Access record corresponding to current row index
        Record_pds = pdf.iloc[Record_Index]
        
        #Convert record to SQL readable
        SQL_Record_Str = '('
        for Column_Index in range(len(Record_pds)):
            
            #Pull column value from record
            Value = Record_pds.iloc[Column_Index]
            
            #Adjust SQL statement for data type
            if type(Value) == str:
                SQL_Record_Str += "'" + Value + "'" + ','
                pass
            elif type(Value) == np.int64 or type(Value) == np.float64:
                SQL_Record_Str += str(Value) + ','
                pass
            elif type(Value) == pd._libs.tslibs.timestamps.Timestamp:
                Yr = str(Value.year)
                Mo = str(Value.month)
                Day = str(Value.day)
                Hr = str(Value.hour)
                Min = str(Value.minute)
                Sec = str(Value.second)
                Date_Str = Yr + '-' + Mo + '-' + Day + ' '
                Date_Str += Hr + ':' + Min + ':' + Sec
                SQL_Record_Str += "CAST('" + Date_Str + "' AS datetime),"
                pass
            else:
                print('Data type not recognized in pandas dataframe row:' + str(Record_Index))
                pass
            continue
        #Replace final comma with closing parentheses
        SQL_Record_Str = SQL_Record_Str[:len(SQL_Record_Str) - 1]
        SQL_Record_Str += ')'
        
        
        #Append record to list of records
        SQL_Records_Str += SQL_Record_Str + ','
        continue
    
    #Replace final comma with semi-colon
    SQL_Records_Str = SQL_Records_Str[:len(SQL_Records_Str) - 1]
    SQL_Records_Str += ';'
    
    
    #Combine SQL string
    SQL_Final_Str = 'INSERT INTO ' + Table_Name + ' ' + SQL_Var_Names_Str + ' VALUES ' + SQL_Records_Str
    
    #Execute and commit SQL statement
    Cursor.execute(SQL_Final_Str)
    Connection.commit()
    return



