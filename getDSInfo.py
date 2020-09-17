### Conexión a la consola
connect('weblogic','Welcome1','t3://192.168.0.30:7001')


cd('/')
#
#Obtiene todos los DataSources
dss = cmo.getJDBCSystemResources()

def getJDBCConnectionPoolParams(dsName):
	#obtencion de informacion
	cd('JDBCSystemResources/'+dsName+'/JDBCResource/'+dsName+'/JDBCConnectionPoolParams/'+dsName)
	InitialCapacity = cmo.getInitialCapacity()
	MaxCapacity = cmo.getMaxCapacity()
	MinCapacity = cmo.getMinCapacity()
	InactiveConnectionTimeoutSeconds = cmo.getInactiveConnectionTimeoutSeconds()
	#impresiones
	print "InitialCapacity: "+str(InitialCapacity)
	print "MaxCapacity: "+str(MaxCapacity)
	print "MinCapacity: "+str(MinCapacity)
	print "InactiveConnectionTimeoutSeconds: "+str(InactiveConnectionTimeoutSeconds)
	cd('/')
	
def getJDBCXAParams(dsName):
	cd('/JDBCSystemResources/'+dsName+'/JDBCResource/'+dsName+'/JDBCXAParams/'+dsName)
	XaSetTransactionTimeout = get('XaSetTransactionTimeout')
	XaTransactionTimeout = cmo.getXaTransactionTimeout()
	XaSet = 'False'
	if XaSetTransactionTimeout == 1:
		XaSet = 'True'
	print 'XaSetTransactionTimeout: '+str(XaSet)
	print 'XaTransactionTimeout: '+str(XaTransactionTimeout)
	cd('/')
	
def getJDBCDataSourceParams(dsName):
	cd('/JDBCSystemResources/'+dsName+'/JDBCResource/'+dsName+'/JDBCDataSourceParams/'+dsName)
	#Obtiene los JNDI asignados al DS
	JNDINames = cmo.getJNDINames()
	#Imprime cada JNDI
	for JNDIName in JNDINames:
		print JNDIName
	cd('/')

def getJDBCDriverParams(dsName):
	cd('/JDBCSystemResources/'+dsName+'/JDBCResource/'+dsName+'/JDBCDriverParams/'+dsName)
	Url = cmo.getUrl()
	DriverName = cmo.getDriverName()
	
	print 'Url: '+Url
	print 'DriverName: '+DriverName
	
	cd('Properties/'+dsName)
	properties = cmo.getProperties()
	for property in properties:
		name = property.getName()
		value = property.getValue()
		print name+'='+str(value)
	cd('/')
	
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
	print ''
	
	#Obtiene parametros XA
	separador()
	print 'JDBCXAParams'
	separador()
	getJDBCXAParams(dsName)
	print ''
	
	#Obtiene Parametros de DataSource
	separador()
	print 'JDBCDataSourceParams'
	separador()
	getJDBCDataSourceParams(dsName)
	print ''
	
	#Obtiene los parametros JDBCDriverParams
	separador()
	print 'JDBCDriverParams'
	separador()
	getJDBCDriverParams(dsName)
	print ''