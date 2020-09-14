
connect('weblogic','Welcome1','t3://localhost:7001')
cd('JDBCSystemResources')
dataSources = cmo.getJDBCSystemResources()

for ds in dataSources:
 name = ds.getName()
 print name
 cd(name)
 path = cmo.getSourcePath()
 print 'Archivo de Configuracion: ' + path
 cd('../')
print "Ejecucion de Script Terminada"
