import maya.cmds as cmds
sel_curves = cmds.ls(sl=True, o=True)
if sel_curves:
    shapes_ls = cmds.listRelatives(sel_curves, children=True)
    vtx_ls = []
    for shape in shapes_ls:
        sel_vtx = cmds.ls('{}.controlPoints[:]'.format(shape), fl=True)
        for vtx in sel_vtx:
            vtx_ls.append(vtx)
    cmds.select(vtx_ls)
