import maya.cmds as cmds
def combine_curve():
    change_ls = cmds.ls(sl=True)
    if len(change_ls) >= 2:
        new_control = change_ls[-1]
        change_ls.remove(new_control)
        for curve in change_ls:
            base_shape = cmds.listRelatives(curve, s=True)[0]
            cmds.makeIdentity(curve, apply=True, t=True, r=True, s=True, n=0)
            cmds.makeIdentity(new_control, apply=True, t=True, r=True, s=True, n=0)
            cmds.parent(base_shape, new_control, s=True, relative=True)
            cmds.delete(curve)
combine_curve()