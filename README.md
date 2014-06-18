openshift-origin-websphere-cartridge
====================================

This is a cartridge to integrate the Websphere Application Server with OpenShift. The main focus for this cartridge is OpenShift Enterprise. At this point in time this is rather a Proof of Concept cartridge, as its sole purpose is to demonstrate that an integration is indeed possible. For now this cartridge will only create unmanaged profiles with the default servername `server1`

Requirements
------------

This cartridge needs an existing installation of the WebSpehere Application Server on each of your nodes. You need to define the location of the installation through a system wide environment variable 

```
echo "/opt/IBM/WebSphere/AppServer" > /etc/openshift/env/OPENSHIFT_WEBSPHERE_INSTALL_LOCATION
```

this will make sure that the cartridge finds the necessary components.

How this cartridge works
------------------------

This cartridge will call `${OPENSHIFT_WEBSPHERE_DIR}/install/bin/manageprofiles.sh` and create a profile with the name ${OPENSHIFT_APP_NAME}. The profile will be created underneath the `profile` directory inside your gears `data` directory. 

The profile will have security enabled. An admin `username` and a `password` are generated at the time of creation and the `PerfTuningSetting` will be set to development.

Installation of the cartridge
-----------------------------

```
# oo-admin-cartridge --action install --source https://github.com/juhoffma/openshift-origin-websphere-cartridge.git
# oo-admin-ctl-cartridge --activate -c import-node --obsolete
# oo-admin-broker-cache --clear && oo-admin-console-cache --clear
```

ToDo's
------

[ ] Work with managed profiles
[ ] Support Marker Files for different JDK's
[ ] Enable Deployments through deployable apps
[ ] Provide a build lifecycle a la JBoss Cartridge
