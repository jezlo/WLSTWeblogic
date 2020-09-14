connect('weblogic','Welcome1','t3://192.168.0.30:7001')

cd('JDBCSystemResources/SOADataSource/JDBCResource/SOADataSource/JDBCConnectionPoolParams/SOADataSource')
ic = cmo.getInitialCapacity()
max = cmo.getMaxCapacity()
min = cmo.getMinCapacity()
icts = cmo.getInactiveConnectionTimeoutSeconds()


print "Las conexiones iniciales son: "+str(ic)
print "Las conexiones Maximas son: "+str(max)
print "Las conexiones minimas son: "+str(min)
print "El timeout de conexion inactiva: "+str(icts) 
