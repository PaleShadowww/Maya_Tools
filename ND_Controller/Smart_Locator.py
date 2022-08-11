import maya.cmds as cmds
list_objects = cmds.ls(sl=True)
if list_objects:
    for main_object in list_objects:
        locator = cmds.spaceLocator(n='Locator_ND')
        if cmds.objectType(main_object) != "joint":
            bbox = cmds.exactWorldBoundingBox(main_object)
            loc_size = (bbox[3] - bbox[0]) * 0.77
            cmds.setAttr('Locator_NDShape.localScaleX', loc_size)
            cmds.setAttr('Locator_NDShape.localScaleY', loc_size)
            cmds.setAttr('Locator_NDShape.localScaleZ', loc_size)
        cmds.matchTransform(locator, main_object)
        cmds.select(locator)
        cmds.rename(locator, "locator1")
else:
    cmds.spaceLocator()