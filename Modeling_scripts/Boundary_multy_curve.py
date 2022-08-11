import maya.cmds as cmds


def extra_curve():
    list_curve = cmds.ls(sl=True, o=True)
    if len(list_curve) < 5:
        cmds.boundary(list_curve, order=False, ch=1, ept=0.01, po=0, rn=0, ep=0)
    else:
        list_curve.sort()
        curve_0, curve_1, curve_2 = list_curve[0], list_curve[1], list_curve[2]
        for n in range(3):
            list_curve.remove(list_curve[0])
        cmds.attachCurve(list_curve, method=0, rpo=False, n="curve_omega_ND_ID")
        cmds.boundary('curve_omega_ND_ID', curve_0, curve_1, curve_2, order=False, ch=1, ept=0.01, po=0, rn=0, ep=0)
        cmds.delete('curve_omega_ND_ID')


extra_curve()


