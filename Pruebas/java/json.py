#!/usr/bin/python
# Author : Tim Hall
# Save Script as : create_data_source.py

import time
import getopt
import sys
import re

# Get location of the properties file.
properties = ''
try:
   opts, args = getopt.getopt(sys.argv[1:],"p:h::",["properies="])
except getopt.GetoptError:
   print 'set_datasource.py -p <path-to-properties-file>'
   sys.exit(2)
for opt, arg in opts:
   if opt == '-h':
      print 'set_datasource.py -p <path-to-properties-file>'
      sys.exit()
   elif opt in ("-p", "--properties"):
      properties = arg
print 'properties=', properties

# Load the properties from the properties file.
from java.io import FileInputStream
 
propInputStream = FileInputStream(properties)
configProps = Properties()
configProps.load(propInputStream)
ds="SOA"
# Set all variables from values in properties file.
adminUsername=configProps.get(ds+"admin.username")
adminPassword=configProps.get("admin.password")
adminURL=configProps.get("admin.url")
dsName=configProps.get("ds.name")
dsJNDIName=configProps.get("ds.jndi.name")
dsURL=configProps.get("ds.url")
dsDriver=configProps.get("ds.driver")
dsUsername=configProps.get("ds.username")
dsPassword=configProps.get("ds.password")
dsTargetType=configProps.get("ds.target.type")
dsTargetName=configProps.get("ds.target.name")

# Display the variable values.
print 'adminUsername=', adminUsername
print 'adminPassword=', adminPassword
print 'adminURL=', adminURL
print 'dsName=', dsName
print 'dsJNDIName=', dsJNDIName
print 'dsURL=', dsURL
print 'dsDriver=', dsDriver
print 'dsUsername=', dsUsername
print 'dsPassword=', dsPassword
print 'dsTargetType=', dsTargetType
print 'dsTargetName=', dsTargetName

configProps.set(dsUsername, "web")
