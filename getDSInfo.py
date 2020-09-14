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
	print "Los parametros del Datasource "+dsName+" son:"
	print "Las conexiones iniciales son: "+str(InitialCapacity)
	print "Las conexiones Maximas son: "+str(MaxCapacity)
	print "Las conexiones minimas son: "+str(MinCapacity)
	print "El timeout de conexion inactiva: "+str(InactiveConnectionTimeoutSeconds)

for ds in dss:
	dsName = ds.getName()
	getJDBCConnectionPoolParams(dsName)

	cd('/')
