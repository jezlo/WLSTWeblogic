#import json

### Creación de Array para JSON
data = {}
data['dataSources'] = []

### Conexión a la consola
connect('weblogic','Welcome1','t3://192.168.0.30:7001')


cd('/')

#Se obtiene los parametros de JDBCSystemResources
dss = cmo.getJDBCSystemResources()

def getJDBCConnectionPoolParams(dsName):
	cd('JDBCSystemResources/'+dsName+'/JDBCResource/'+dsName+'/JDBCConnectionPoolParams/'+dsName)
	InitialCapacity = cmo.getInitialCapacity()
	MaxCapacity = cmo.getMaxCapacity()
	MinCapacity = cmo.getMinCapacity()
	InactiveConnectionTimeoutSeconds = cmo.getInactiveConnectionTimeoutSeconds()
	print "InitialCapacity: "+str(InitialCapacity)
	print "MaxCapacity: "+str(MaxCapacity)
	print "MinCapacity: "+str(MinCapacity)
	print "InactiveConnectionTimeoutSeconds: "+str(InactiveConnectionTimeoutSeconds)
	print ''
	
def getJDBCXAParams(dsName):
	cd('/JDBCSystemResources/'+dsName+'/JDBCResource/'+dsName+'/JDBCXAParams/'+dsName)
	XaSetTransactionTimeout = get('XaSetTransactionTimeout')
	XaTransactionTimeout = cmo.getXaTransactionTimeout()
	print 'XaSetTransactionTimeout: '+XaSetTransactionTimeout
	print 'XaTransactionTimeout: '+XaTransactionTimeout
	
	
	
def separador():
	print '-------------------------'

for ds in dss:
	dsName = ds.getName()
	print 'JDBCConnectionPoolParams'
	separador()
	print "Los parametros del Datasource "+dsName+" son:"
	getJDBCConnectionPoolParams(dsName)
	cd('/')
	separador()
	print ''
	print 'JDBCXAParams'
	getJDBCXAParams(dsName)
	
