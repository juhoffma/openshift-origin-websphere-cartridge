c1 = AdminConfig.getid('/Cell:OpenShiftCell/')
md = AdminConfig.showAttribute(c1, "monitoredDirectoryDeployment")
AdminConfig.modify(md, [['enabled', "true"]])
AdminConfig.save()
