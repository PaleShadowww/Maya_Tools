import maya.cmds as cmds
def make_extra_gr():
    obj_list = cmds.ls(sl=True)
    if obj_list:
        for obj in obj_list:
            i = 1
            while cmds.objExists(obj + '_' + str(i) + '_extra'):
                i += 1
            cmds.group(em=True, n=obj + '_' + str(i) + '_extra')
            cmds.matchTransform(obj + '_' + str(i) + '_extra', obj, scl=False)
            up = cmds.listRelatives(obj, parent=1, fullPath=1)[0]
            cmds.parent(obj + '_' + str(i) + '_extra', up)
            cmds.reorder(obj + '_' + str(i) + '_extra', relative=i)
            cmds.parent(obj, obj + '_' + str(i) + '_extra')
    cmds.select(obj_list)
make_extra_gr()