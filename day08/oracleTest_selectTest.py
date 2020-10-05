import cx_Oracle
import os


os.putenv('NLS_LANG', '.UTF8')

# conn = cx_Oracle.connect('SHS', 'java', 'localhost/xe')
conn = cx_Oracle.connect('SHS/java@localhost:1521/xe')
cursor = conn.cursor()

cursor.execute('select BUYER_ID, '
                        + 'BUYER_NAME, '
                        + 'BUYER_LGU, '
                        + 'BUYER_BANK, '
                        + 'BUYER_BANKNO, '
                        + 'BUYER_BANKNAME, '
                        + 'BUYER_ZIP, '
                        + 'BUYER_ADD1, '
                        + 'BUYER_ADD2, '
                        + 'BUYER_COMTEL, '
                        + 'BUYER_FAX, '
                        + 'BUYER_MAIL, '
                        + 'BUYER_CHARGER, '
                        + 'BUYER_TELEXT '
                        + 'from buyer')


for buyerInfo in cursor:
    print(buyerInfo[0], buyerInfo[1], buyerInfo[2])
    
    
    
    
    
    
    
    
    
    
    
cursor.execute('select * from temp02')
for temp in cursor:
    print(temp)    
    
