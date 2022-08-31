
"""
user = 'root'
passw = 'root'
host =  'localhost'
port = 3306
database = 'pfdb'
#dtype={'Col_1':string, 'value': int}
conn = pymysql.connect(host=host, port=port, user=user, passwd=passw, db=database, charset='utf8')

#df_fpf1_comm_overview_2.to_sql(con=conn, name='pf_kpi_summary_temp', if_exists = 'append')

#data = pd.read_sql('SELECT * FROM pf_kpi_summary', conn)
#print(data)
#data.to_sql(con=conn, name='pf_kpi_summary_temp', if_exists = 'append')
#kpi_id                         name      value unit        date

connection_string = 'mysql+pymysql://{}:{}@{}/{}'.format('root','root','localhost','pfdb')
engine = create_engine(connection_string)

# IMPORT DATA INTO DATA FRAME
data = pd.read_sql('SELECT * FROM pf_kpi_summary', engine)
print(data)
# SQL DELETE (CLEAN OUT TABLE) VIA TRANSACTION
#with engine.begin() as conn:     conn.execute("DELETE FROM some_table")

# MIGRATE DATA INTO DATA FRAME (APPEND NOT REPLACE)
#data.to_sql(name='pf_kpi_summary_temp', con=engine, if_exists='append', index=False)
#sql = "INSERT INTO customers (name, value, unit, date) VALUES (%s, %s, %s, %s)"
#val = df_fpf1_comm_overview_2
#dtype = {"name": String(), "value": Integer(), "unit": String(), "date": Date()}
#df_fpf1_comm_overview_2.to_sql(name='pf_kpi_summary_temp', con=engine, if_exists='append', index=False)
"""