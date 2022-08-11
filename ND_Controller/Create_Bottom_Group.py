import maya.cmds as cmds
def make_bot_gr():
    obj_list = cmds.ls(sl=True)
    if obj_list:
        for obj in obj_list:
            i = 1
            while cmds.objExists(obj + '_' + str(i) + '_bot'):
                i += 1
            cmds.group(em=True, n=obj + '_' + str(i) + '_bot')
            cmds.matchTransform(obj + '_' + str(i) + '_bot', obj, scl=False)
            cmds.parent(obj + '_' + str(i) + '_bot', obj)
            cmds.reorder(obj + '_' + str(i) + '_bot', relative=i)
    cmds.select(obj_list)
make_bot_gr()