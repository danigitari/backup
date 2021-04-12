import os

HOST='localhost'
PORT='3306'
DB_USER='test_a'
DB_PASS='12345678'

os.popen("mysqldump -h %s -P %s -u %s -p%s %s > %s.sql" % (HOST,PORT,DB_USER,DB_PASS,'up_saas','backup'))