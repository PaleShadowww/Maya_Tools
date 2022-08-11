import maya.cmds as cmds
def create_curve_command():
    sel_list = cmds.ls(sl=True, o=True)
    for sel in sel_list:
        sel_shape = cmds.listRelatives(sel, s=True)[0]
        degree = str(cmds.getAttr(sel_shape + ".degree"))
        sel_vtx = cmds.ls('{}.controlPoints[:]'.format(sel), fl=True)
        cmds.select(sel_vtx)
        i = 0
        all_vtx_list = []
        for vtx in sel_vtx:
            cmds.select(vtx)
            x = float("%.4f" % cmds.getAttr(sel_shape + '.controlPoints[' + str(i) + '].xValue'))
            y = float("%.4f" % cmds.getAttr(sel_shape + '.controlPoints[' + str(i) + '].yValue'))
            z = float("%.4f" % cmds.getAttr(sel_shape + '.controlPoints[' + str(i) + '].zValue'))
            all_vtx_list.append((x, y, z))
            i += 1
        print (all_vtx_list)
        sys.stdout.write(str('cmds.curve(d=' + degree + ', n="' + sel + '", p=' + str(all_vtx_list) + ')'))
    cmds.select(sel_list)
create_curve_command()