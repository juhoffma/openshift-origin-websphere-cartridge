#!/bin/bash -e
OPENSHIFT_WEBSPHERE_INSTALL_LOCATION="/opt/IBM/WebSphere/AppServer"
echo $OPENSHIFT_WEBSPHERE_INSTALL_LOCATION
chmod a+wr $OPENSHIFT_WEBSPHERE_INSTALL_LOCATION/logs/manageprofiles
chmod -R a+wr $OPENSHIFT_WEBSPHERE_INSTALL_LOCATION/properties
chmod a+wr $OPENSHIFT_WEBSPHERE_INSTALL_LOCATION/properties/fsdb
chmod a+wr $OPENSHIFT_WEBSPHERE_INSTALL_LOCATION/properties/profileRegistry.xml
chmod -R a+r $OPENSHIFT_WEBSPHERE_INSTALL_LOCATION/profileTemplates
chmod -R a+rw $OPENSHIFT_WEBSPHERE_INSTALL_LOCATION/configuration
chmod -R a+rwx $OPENSHIFT_WEBSPHERE_INSTALL_LOCATION/configuration/org.eclipse.osgi/.manager/.*
