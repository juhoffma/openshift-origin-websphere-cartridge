###############################################################################
# READ CLI ARGUMENTS
###############################################################################
OPENSHIFT_GEAR_DNS = sys.argv[0]
OPENSHIFT_WEBSPHERE_IP = sys.argv[1]

###############################################################################
# Enable Monitored Deployment
###############################################################################
c1 = AdminConfig.getid('/Cell:OpenShiftCell/')
md = AdminConfig.showAttribute(c1, "monitoredDirectoryDeployment")
AdminConfig.modify(md, [['enabled', "true"]])

###############################################################################
# Set GEAR hostname for all virtual hosts
###############################################################################
vhosts = AdminConfig.list('VirtualHost').split(java.lang.System.getProperty("line.separator"))
for vhost in vhosts:
	endpointString = AdminConfig.showAttribute(vhost, "aliases")
	endpointList = endpointString[1:len(endpointString)-1].split(" ")
	for endpoint in endpointList:
		AdminConfig.modify(endpoint, '[[hostname "' + OPENSHIFT_GEAR_DNS + '"]]')

###############################################################################
# Configure WebSphere to use a specific IP address
# http://www-01.ibm.com/support/knowledgecenter/SSAW57_8.5.5/com.ibm.websphere.nd.doc/ae/trun_multiplenic.html?lang=en
###############################################################################
# Customize ORB service
orb = AdminConfig.list('ObjectRequestBroker')
orbPropertiesString = AdminConfig.showAttribute(orb, "properties")
orbPropertiesList = orbPropertiesString[1:len(orbPropertiesString)-1].split(" ")
# Remove specific existing properties
for orbProperty in orbPropertiesList:
	name = AdminConfig.showAttribute(orbProperty, "name")
	if name == "com.ibm.CORBA.LocalHost":
		AdminConfig.remove(orbProperty)
	elif name == "com.ibm.ws.orb.transport.useMultiHome":
		AdminConfig.remove(orbProperty)

# Add new properties
attr = []
attr.append([['name','com.ibm.CORBA.LocalHost'],['required','true'],['value', OPENSHIFT_WEBSPHERE_IP]])
AdminConfig.modify(orb, [['properties', attr]])
attr = []
attr.append([['name','com.ibm.ws.orb.transport.useMultiHome'],['required','false'],['value','false']])
AdminConfig.modify(orb, [['properties', attr]])

# Customize JVM custom properties
jvm = AdminConfig.list('JavaVirtualMachine')
jvmPropertiesString = AdminConfig.showAttribute(jvm, "systemProperties")
jvmPropertiesList = jvmPropertiesString[1:len(jvmPropertiesString)-1].split(" ")
# Remove specific existing properties
for jvmProperty in jvmPropertiesList:
	name = AdminConfig.showAttribute(jvmProperty, "name")
	if name == "com.ibm.websphere.network.useMultiHome":
		AdminConfig.remove(jvmProperty)

# Add new properties
attr = []
attr.append([['name','com.ibm.websphere.network.useMultiHome'],['required','false'],['value', 'false']])
AdminConfig.modify(jvm, [['systemProperties', attr]])

# Bind all ports to GEAR IP
endpoints = AdminConfig.list('EndPoint').split(java.lang.System.getProperty("line.separator"))
for endpoint in endpoints:
	AdminConfig.modify(endpoint, '[[host ' + OPENSHIFT_WEBSPHERE_IP + ']]')

###############################################################################
AdminConfig.save()
