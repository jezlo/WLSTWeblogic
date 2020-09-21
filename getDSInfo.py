def getDS():
	### Conexion a la consola
	connect('weblogic','Welcome1','t3://192.168.0.30:7001')

	cd('/')
	#Obtiene todos los DataSources
	dss = cmo.getJDBCSystemResources()
	return dss

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
		print 'JNDIName: 'JNDIName
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

def menuDS():
	dsName = ds.getName()
	print "Menu DS"

def menu():
	dss = getDS()
	listaDataSources = ['Salir']
	contador = 0

	for ds in dss:
		dsName = ds.getName()
		listaDataSources.append(dsName)

	for i in listaDataSources:
		print str(contador)+". "+i
		contador += 1
	while True:
		print 'options...'
		choice = int(raw_input())
		dsName = listaDataSources[choice]
		if choice == 0:
			break
		else:
			getJDBCConnectionPoolParams(dsName)
			getJDBCXAParams(dsName)
			getJDBCDataSourceParams(dsName)
			getJDBCDriverParams(dsName)

#Ciclo sobre todos los DataSources
def allInfo():
	dss = getDS()
	for ds in dss:
		#Obtiene Nombre de los DataSources
		dsName = ds.getName()
		
		#Imprime el Nombre del DataSource
		separador2()
		print "##### "+dsName
		separador2()
		print ''
		
		#Obtiene parametros de Conexion
		getJDBCConnectionPoolParams(dsName)
		print ''
		
		#Obtiene parametros XA
		getJDBCXAParams(dsName)
		print ''
		
		#Obtiene Parametros de DataSource
		getJDBCDataSourceParams(dsName)
		print ''
		
		#Obtiene los parametros JDBCDriverParams
		getJDBCDriverParams(dsName)
		print ''
menu()
print "Finalizo el Script"