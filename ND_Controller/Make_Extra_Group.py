import maya.cmds as cmds


def make_extra_gr():
        transf = cmds.ls(sl=True)
        i = 1
        while cmds.objExists(transf[0] + '_' + str(i) + '_extra'):
                i += 1

        cmds.group(em=True, n=transf[0] + '_' + str(i) + '_extra')
        cmds.matchTransform(transf[0] + '_' + str(i) + '_extra', transf, scl=False)
        up = cmds.listRelatives(transf, parent=1, fullPath=1)[0]
        cmds.parent(transf[0] + '_' + str(i) + '_extra', up)
        cmds.reorder(transf[0] + '_' + str(i) + '_extra', relative=i)
        cmds.parent(transf, transf[0] + '_' + str(i) + '_extra')
        cmds.select(transf)


make_extra_gr()

