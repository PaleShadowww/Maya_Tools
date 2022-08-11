import maya.cmds as cmds
def add_curve():
    targets_ls = cmds.ls(sl=True)
    if len(targets_ls) >= 2:
        source = targets_ls[0]
        targets_ls.remove(source)
        for curve in targets_ls:
            target_shape = cmds.listRelatives(curve, f=True, s=True)
            source_shape = cmds.listRelatives(source, f=True, s=True)[0]
            set_width = cmds.getAttr(source_shape+".lineWidth")
            color_sours = cmds.getAttr(source_shape + ".overrideColor")
            cmds.duplicateCurve(source_shape, name='Source_Curve_ND', constructionHistory=False)
            list_sets = cmds.listSets(object=target_shape[0])
            cmds.parent('Source_Curve_NDShape', curve, shape=True, relative=True)
            cmds.delete('Source_Curve_ND')
            cmds.setAttr("Source_Curve_NDShape.overrideEnabled", True)
            cmds.setAttr("Source_Curve_NDShape.overrideColor", color_sours)
            cmds.setAttr("Source_Curve_NDShape.lineWidth", set_width)
            cmds.rename('Source_Curve_NDShape', curve + 'Shape')
            new_shape = cmds.ls(sl=True)
            if list_sets:
                for in_set in list_sets:
                    cmds.sets(new_shape, add=in_set)
            cmds.select(curve)
add_curve()