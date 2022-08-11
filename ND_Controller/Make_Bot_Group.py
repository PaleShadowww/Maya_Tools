import maya.cmds as cmds


def make_bot_gr():
    transf = cmds.ls(sl=True)
    i = 1
    while cmds.objExists(transf[0] + '_' + str(i) + '_bot'):
        i += 1

    cmds.group(em=True, n=transf[0] + '_' + str(i) + '_bot')
    cmds.matchTransform(transf[0] + '_' + str(i) + '_bot', transf, scl=False)
    cmds.parent(transf[0] + '_' + str(i) + '_bot', transf)
    cmds.reorder(transf[0] + '_' + str(i) + '_bot', relative=i)
    cmds.select(transf)


make_bot_gr()

