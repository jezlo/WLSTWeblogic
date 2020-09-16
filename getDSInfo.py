### Conexión a la consola
connect('weblogic','Welcome1','t3://192.168.0.30:7001')


cd('/')
#
#Obtiene todos los DataSources
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
	
def getJDBCXAParams(dsName):
	cd('/JDBCSystemResources/'+dsName+'/JDBCResource/'+dsName+'/JDBCXAParams/'+dsName)
	XaSetTransactionTimeout = get('XaSetTransactionTimeout')
	XaTransactionTimeout = cmo.getXaTransactionTimeout()
	print 'XaSetTransactionTimeout: '+str(XaSetTransactionTimeout)
	print 'XaTransactionTimeout: '+str(XaTransactionTimeout)
	
def getJDBCDataSourceParams(dsName):
	cd('/JDBCSystemResources/'+dsName+'/JDBCResource/'+dsName+'/JDBCDataSourceParams/'+dsName)
	#Obtiene los JNDI asignados al DS
	JNDINames = cmo.getJNDINames()
	#Imprime cada JNDI
	for JNDIName in JNDINames:
		print JNDIName

def getJDBCDriverParams(dsName):
	cd('/JDBCSystemResources/'+dsName+'/JDBCResource/'+dsName+'/JDBCDriverParams/'+dsName)
	Url = cmo.getUrl()
	print Url
	
	cd('Properties/'+dsName)
	properties = cmo.getProperties()
	for property in properties:
		name = property.getName()
		value = property.getValue()
		print name+'='+str(value)
	
	
def separador():
	print '-------------------------'
	
def separador2():
	print '#########################'

#Ciclo sobre todos los DataSources
for ds in dss:
	#Obtiene Nombre de los DataSources
	dsName = ds.getName()
	
	#Imprime el Nombre del DataSource
	separador2()
	print "##### "+dsName
	separador2()
	print ''
	
	#Obtiene parametros de Conexion
	separador()
	print 'JDBCConnectionPoolParams'
	separador()
	getJDBCConnectionPoolParams(dsName)
	cd('/')
	print ''
	
	#Obtiene parametros XA
	separador()
	print 'JDBCXAParams'
	separador()
	getJDBCXAParams(dsName)
	cd('/')
	print ''
	
	#Obtiene Parametros de DataSource
	separador()
	print 'getJDBCDataSourceParams'
	separador()
	getJDBCDataSourceParams(dsName)
	cd('/')
	print ''
	
	#Obtiene los parametros JDBCDriverParams
	separador()
	print 'getJDBCDriverParams'
	separador()
	getJDBCDriverParams(dsName)
	print ''