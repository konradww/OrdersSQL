import pyodbc
# -*- coding: utf-8 -*-
import json
import logging
import io
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# i added data to file JSON
# data = {'server' : 'localhost',
#         'database' : 'TEST',
#         'username' : 'sa',
#         'password' : '********'
#         }
# with io.open('data.json', 'w', encoding='utf8') as outfile:
#     outfile.write(json.dumps(data,
#                              sort_keys=False,
#                              ensure_ascii=False,
#                              indent=4))

with open('data.json') as data_file:
    data_loaded = json.load(data_file)
# logging.debug(data_loaded['password'])
#
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};'
                      'SERVER='+data_loaded['server']
                      +';PORT=1443;DATABASE='
                      +data_loaded['database']
                      +';UID='+data_loaded['username']
                      +';PWD='+ data_loaded['password'])
cursor = cnxn.cursor()
# test SQL
# cursor.execute("select * from dbo.cust")
# for row in cursor.fetchall():
#     logging.debug(row)
# cursor.execute("select * from dbo.product")
# cursor.execute("insert into dbo.product(nameProduct) values ('tomato')")

class shop(object):
    def addproduct(self, nameproduct):
        question = ("IF NOT EXISTS (SELECT * FROM dbo.product WHERE nameProduct like '%s')"
                    "BEGIN "
                    "insert into dbo.product(nameProduct) values ('%s') "
                    "END" % (nameproduct, nameproduct))
        return question


    def addcustomer(self, Company, ContactName, Address, City, Telephone, Mail, NIP):
        question = ("IF NOT EXISTS (SELECT * FROM dbo.customer WHERE NIP = %i) "
                    "BEGIN "
                    "insert into dbo.customer(Company, ContactName, Address, City, Telephone, Mail, NIP) "
                    "values ('%s', '%s', '%s', '%s', '%s', '%s', %i) "
                    "END" % (NIP, Company, ContactName, Address, City, Telephone, Mail, NIP))
        return question


obj = shop()
cursor.execute(obj.addproduct('tomato'))
cursor.commit()
cursor.execute(obj.addcustomer('Trek', 'Edward', 'Gromska 15', 'Gdynia', '604500700', 'edwardgromski@gmail.com', 1111))
cursor.commit()
