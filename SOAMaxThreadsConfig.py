#//http://rreddy.blogspot.com/2016/10/wlst-script-to-change.html
import javax.management.openmbean.CompositeDataSupport;
if __name__ == '__main__':
    from wlstModule import *#@UnusedWildImport
print 'starting the script ....'
username = 'weblogic'
password = 'Welcome1'
url='t3://locahost:7001'
connect(username,password,url)
servers = cmo.getServers()
domainRuntime()
for server in servers:
    serverName = server.getName()
    print 'server: ' + server.getName()
    SoaInfraConfigobj = ObjectName('oracle.as.soainfra.config:Location=AdminServer,name=soa-infra,type=SoaInfraConfig,Application=soa-infra')
    print 'Common Properties for soa_server1'
   
    print  mbs.getAttribute(SoaInfraConfigobj, 'GlobalTxRetryInterval')
    props1 = mbs.getAttribute(SoaInfraConfigobj, 'SOAMaxThreadsConfig')
    print props1.get("incomingRequestsPercentage")
    print props1.get("internalBufferPercentage")
    print props1.get("internalProcessingPercentage")
   
    print props1
   
    javaMap = java.util.HashMap()
    javaMap.put("incomingRequestsPercentage", java.lang.Integer(20))
    javaMap.put("internalBufferPercentage", java.lang.Integer(40))
    javaMap.put("internalProcessingPercentage", java.lang.Integer(40))
    print javaMap
   
    mbs.setAttribute(SoaInfraConfigobj, Attribute('GlobalTxRetryInterval', 22))
    print  mbs.getAttribute(SoaInfraConfigobj, 'GlobalTxRetryInterval')
   
    new_rec_config_obj = javax.management.openmbean.CompositeDataSupport(props1.getCompositeType(),javaMap)
    print new_rec_config_obj
   
    mbs.setAttribute(SoaInfraConfigobj, Attribute('SOAMaxThreadsConfig', new_rec_config_obj))
   
   
    props1 = mbs.getAttribute(SoaInfraConfigobj, 'SOAMaxThreadsConfig')
    print props1.get("incomingRequestsPercentage")
    print props1.get("internalBufferPercentage")
    print props1.get("internalProcessingPercentage")
