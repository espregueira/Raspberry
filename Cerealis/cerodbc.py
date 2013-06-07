import pyodbc

#cnxn = pyodbc.connect('DRIVER={FreeTDS};SERVER=SRV26DEV;DATABASE=Raspberry;UID=rasp;PWD=piroot')
#cnxn = pyodbc.connect('DRIVER={TDS};SERVER=SRV26\development;DATABASE=Raspberry;UID=rasp;PWD=piroot')
cnxn = pyodbc.connect('DSN=SRV26DEV;UID=rasp;PWD=piroot')
cur = cnxn.cursor()
cur.execute('SELECT sensorid, sensor_name FROM sensores')
#row = cur.fetchone()
#if row:
#	print '%s' % row

rows = cur.fetchall()
for row in rows:
    print row.sensorid, row.sensor_name